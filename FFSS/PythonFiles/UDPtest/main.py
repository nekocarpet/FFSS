import socket
import time

# Server details
UDP_IP = "127.0.0.1"
UDP_PORT = 4242

# Messages to be sent
messages = [
    b"1,720,750",
    b"1,500,100|2,100,100",
    b"1,500,100|2,300,340|3,100,200|",
    b"1,350,250|2,100,340|3,130,250|5,270,380",
    b"1,350,250|2,100,380|3,140,450|4,580,350|5,270,380",
    b"1,380,150|2,100,125|3,150,550|4,550,450|5,230,350",
    b"1,400,110|2,100,125|3,170,650|4,450,150|5,220,400",
    b"1,500,260|2,130,325|3,140,550|4,250,250|5,210,450",
    b"1,450,280|2,150,525|3,155,350|4,100,750|5,200,500",
    b"1,400,240|2,160,575|3,125,250|5,200,500",
    b"1,400,240|2,160,575|3,125,250|5,100,500",
    b"1,400,240|2,160,575|3,200,250|5,200,500",
    b"1,400,240|2,160,575|3,200,250"
]

# Interval between each message
INTERVAL = 2  # Adjust this variable as needed for different intervals

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