from ultralytics import YOLO
import supervision as sv
import numpy as np
import os
import tqdm
import cv2

"""
names: 
{
0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 
4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 
8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 
12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 
16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 
20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 
24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 
28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 
32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 
36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 
40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 
44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 
48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 
52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 
56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 
60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 
64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 
68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 
72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 
76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'
}
"""

model = YOLO(r"C:\yolo\pertrained_models\yolov8n.pt", task='detect')

def process_frame(frame: np.ndarray, index, classes_select) -> np.ndarray:
    results = model.predict(frame, verbose=False, classes=classes_select)[0] # person
    detections = sv.Detections.from_ultralytics(results,)
    box_annotator = sv.BoxAnnotator(thickness=4, text_thickness=2, text_scale=0.5)
    labels = [f"{model.names[class_id]} confidence: {confidence:0.2f}, bbox center: ({(xyxy[0]+xyxy[2])/2:0.2f}, {(xyxy[1]+xyxy[3])/2:0.2f})" for xyxy, _, confidence, class_id, _ in detections]
    frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels)
    return frame, detections

def process_video(source_path, target_path, classes_select=[0]):
    source_video_info = sv.VideoInfo.from_video_path(video_path=source_path)
    with sv.VideoSink(target_path=target_path, video_info=source_video_info) as sink:
        for index, frame in tqdm.tqdm(enumerate(
            sv.get_video_frames_generator(source_path=source_path)
        )):
            result_frame, detections = process_frame(frame, index, classes_select)
            sink.write_frame(frame=result_frame)

def process_folder():
    for item in os.listdir('test_inputs'):
        video_path = fr"C:\yolo\test_inputs\{item}"
        if not os.path.isfile(video_path):continue
        target_path = f"outputs/{os.path.basename(video_path).split('.')[0]}.mp4"
        process_video(video_path, target_path, classes_select=[0])

def process_camera(save=False):
    cap = cv2.VideoCapture(0)
    if save:
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
        shape = (640, 480)
        writer = cv2.VideoWriter("capture.mp4", fourcc, fps, shape)
    
    while cap.isOpened():
        _, frame = cap.read()
        result_frame = process_frame(frame, None, classes_select=[0])
        cv2.imshow('video', result_frame)
        key = cv2.waitKey(1)
        if save:
            writer.write(result_frame)
        if key == ord('q'):
            break
    
    cv2.destroyAllWindows()
    cap.release()
    if save:
        writer.release()
    
process_camera(save=False)

#process_video(r"F:\yolo\test_inputs\test.mp4", "outputs/test.mp4")