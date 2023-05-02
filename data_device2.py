from socket import *
import random

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 7778))
print('Device2 is running')

while True:
    data, addr = sock.recvfrom(BUF_SIZE)
    msg = data.decode()

    if msg == 'quit':
        sock.sendto(b'quit', addr)
        break
    else:
        hb = random.randrange(40, 140)
        step = random.randrange(2000, 6000)
        cal = random.randrange(1000, 4000)
        text = f"{hb} {step} {cal}"
        sock.sendto(text.encode(), addr)

sock.close()
