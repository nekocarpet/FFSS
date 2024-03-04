### I use this application to get lonlat coords and manually update main.py ###
### Could probably be better integrated but I'm lazy ###

import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    # Check if the left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"{x}, {y}")

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

# Define the specific pixel coordinates for the polygon
polygon_points = np.array([
        [535, 117],  # top right
        [98, 105],   # top left
        [16, 263],    # bottom left
        [639, 280]   # bottom right
], np.int32)

# Reshape for cv2.polylines
polygon_points = polygon_points.reshape((-1, 1, 2))

# Set window name
window_name = 'Webcam with Polygon'

# Create a window
cv2.namedWindow(window_name)

# Set mouse callback function for the window
cv2.setMouseCallback(window_name, click_event)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Draw the polygon on the frame
    cv2.polylines(frame, [polygon_points], isClosed=True, color=(0, 255, 0), thickness=3)

    # Display the frame
    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Release the VideoCapture object and close windows
cap.release()
cv2.destroyAllWindows()
