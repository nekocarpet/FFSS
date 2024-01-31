import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 4242
MESSAGE_1 = b"1,500,100"
MESSAGE_2 = b"1,500,100|2,100,100"
MESSAGE_3 = b"1,500,100|2,300,340|3,100,200|"
MESSAGE_4 = b"1,350,250|2,100,340|3,150,250|5,270,380"
MESSAGE_5 = b"1,350,250|2,100,380|3,150,250|4,200,450|5,270,380"
MESSAGE_6 = b"1,350,250|2,100,125|3,150,250|4,200,450|5,240,300"
INTERVAL = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

try:
    while True:
        print("Sending message: %s" % MESSAGE_1)
        sock.sendto(MESSAGE_1, (UDP_IP, UDP_PORT))

        time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("Script interrupted by user. Exiting.")
finally:
    sock.close()