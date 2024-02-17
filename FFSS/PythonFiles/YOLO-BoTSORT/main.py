import os
import socket
import numpy as np
from ultralytics import YOLO
from pixel_mapper import PixelMapper

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

model = YOLO(r"C:\yolo\pretrained_models\yolov8m.pt")

# Server details
UDP_IP = "127.0.0.1"
UDP_PORT = 4242
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Task arg variables
SOURCE = 0
CLASSES = 42
CONF = 0.1
MAX_DET = 100
NEW_TRACK_THRESH = 0.5
TRACK_BUFFER = 500
IOU = 0.7
VID_STRIDE = 2

# Quad coords for PixelMapper
quad_coords = {
    "lonlat": np.array([
        [1920, 0], # top right
        [0, 0], # top left
        [0, 1080], # bottom left
        [1920, 1080] # bottom right
    ]),
    "pixel": np.array([
        [535, 117],  # top right
        [98, 105],   # top left
        [16, 263],    # bottom left
        [639, 280]   # bottom right
    ])
}
pm = PixelMapper(quad_coords["pixel"], quad_coords["lonlat"])

try:
    results = model.track(source=SOURCE, show=True, classes=CLASSES, device=0, stream=True, tracker="botsort_mod.yaml",
                          persist=True, max_det=MAX_DET, conf=CONF, iou = IOU, save=False, vid_stride = VID_STRIDE)  # return a generator of Results objects
    # Process results generator
    for r in results:
        formatted_data = ""

        if hasattr(r, 'boxes') and r.boxes is not None and r.boxes.id is not None:
            for i, box in enumerate(r.boxes.xyxy):
                id = r.boxes.id[i] if len(r.boxes.id) > i else 'unknown'
                x1, y1, x2, y2 = box.cpu().numpy()  # Convert box coordinates to numpy array and move to CPU if necessary

                # Calculate the center bottom coordinates
                x_center = (x1 + x2) / 2
                y_bottom = y2

                # Remap coordinates using PixelMapper
                remapped_coords = pm.pixel_to_lonlat([x_center, y_bottom])
                x_mapped, y_mapped = remapped_coords[0]

                # Update formatted_data with remapped coordinates
                formatted_data += f"{int(id)},{x_mapped:.2f},{y_mapped:.2f}|"

        # Send the formatted data through UDP
        sock.sendto(formatted_data.encode(), (UDP_IP, UDP_PORT))
        print(formatted_data)

except KeyboardInterrupt:
    print("Process interrupted by user. Closing socket.")
finally:
    formatted_data = f"Closing..."
    sock.close()
    print("Socket closed.")

