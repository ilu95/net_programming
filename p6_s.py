import socket
import random

port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    print('Received: ', msg.decode())
    if random.random() < 0.4:
        print("Packet loss")
    else:
        sock.sendto('ack'.encode(), addr)
