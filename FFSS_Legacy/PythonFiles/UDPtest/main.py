import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 4242
MESSAGE = b"Hello World"
INTERVAL = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

try:
    while True:
        print("Sending message: %s" % MESSAGE)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("Script interrupted by user. Exiting.")
finally:
    sock.close()