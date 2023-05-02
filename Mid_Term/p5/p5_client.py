from socket import *

BUF_SIZE = 1024
LENGTH = 4


while True:
    start = input("device to connect(1, 2, 3 disconnect = quit): ")
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8888))
    temp = 0
    humid = 0
    lumi = 0

    if start == '1':
        s.send(b'1')
        msg = s.recv(BUF_SIZE).decode().split()
        temp = msg[0]
        # temp[0] = int.from_bytes(temp[0], 'big')
        # int(temp[0])

    elif start == '2':
        s.send(b'2')
        msg = s.recv(BUF_SIZE).decode().split()
        humid = msg[1]
        # humid = int.from_bytes(humid, 'big')
        # int(humid)

    elif start == '3':
        s.send(b'3')
        msg = s.recv(BUF_SIZE).decode().split()
        lumi = msg[2]
        # lumi = int.from_bytes(lumi, 'big')
        # int(lumi)

    print(temp, humid, lumi)
    s.close()
