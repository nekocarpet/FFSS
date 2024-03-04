import socket
import time

# Server details
UDP_IP = "127.0.0.1"
UDP_PORT = 4242

# Messages to be sent
import numpy as np

# Circle
cx, cy = 600, 400  # Center
r = 100  # Radius
n_pixels = 6  # Number of person
n_steps = 20  # Number of steps

# Generate messages
messages = []
for step in range(n_steps):
    message = []
    for i in range(n_pixels):
        theta = 2 * np.pi * i / n_pixels + 2 * np.pi * step / n_steps
        x = int(cx + r * np.cos(theta))
        y = int(cy + r * np.sin(theta))
        message.append(f"{i+1},{x},{y}")
    messages.append("|".join(message).encode())

# Interval between each message
INTERVAL = 0.8

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

try:
    while True:
        for message in messages:
            print("Sending message:", message)
            sock.sendto(message, (UDP_IP, UDP_PORT))
            time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("Script interrupted by user. Exiting.")
finally:
    sock.close()