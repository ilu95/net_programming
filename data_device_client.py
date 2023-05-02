from socket import *
import time

BUF_SIZE = 1024
LENGTH = 4

try:
    f = open('data.txt', 'r')

except:
    f = f = open('data.txt', 'w')

f.close()

s = socket(AF_INET, SOCK_DGRAM)

while True:
    start = input("device to connect(1, 2, disconnect = quit): ")

    if start == '1':
        s.sendto(b'Request', ('localhost', 7777))
        msg, addr = s.recvfrom(BUF_SIZE)
        msg = msg.decode().split()
        text = f"{time.asctime()}: Device1: Temp={msg[0]}, Humid={msg[1]}, Lilum={msg[2]}\n"

    elif start == '2':
        s.sendto(b'Request', ('localhost', 7778))
        msg, addr = s.recvfrom(BUF_SIZE)
        msg = msg.decode().split()
        text = f"{time.asctime()}: Device2: Heartbeat={msg[0]}, Steps={msg[1]}, Cal={msg[2]}\n"

    else:
        s.sendto(start.encode(), ('localhost', 7777))
        s.sendto(start.encode(), ('localhost', 7778))
        break

    f = open('data.txt', 'a', encoding='utf-8')
    f.write(text)
    f.close()

s.close()
