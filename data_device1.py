from socket import *
import random

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 7777))
print('Device1 is running')

while True:
    msg, addr = sock.recvfrom(BUF_SIZE)
    msg = msg.decode()

    if msg == 'quit':
        sock.sendto(b'quit', addr)
        break
    else:
        temp = random.randrange(0, 40)
        humid = random.randrange(0, 100)
        lilum = random.randrange(70, 150)
        text = f"{temp} {humid} {lilum}"
        sock.sendto(text.encode(), addr)

sock.close()
