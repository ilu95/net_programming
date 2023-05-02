from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4  # '파일 크기': 4바이트

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 7777))

print('File server is running...')

while True:
    try:
        msg, addr = sock.recvfrom(BUF_SIZE)
    except timeout:
        continue

    filename = msg.decode()
    print('client:', addr, filename)

    try:
        filesize = os.path.getsize(filename)
    except:
        sock.sendto(b'Nofile', addr)
        continue
    else:
        # 파일 크기 전송
        fs_binary = filesize.to_bytes(LENGTH, 'big')
        sock.sendto(fs_binary, addr)

    f = open(filename, 'rb')
    data = f.read(BUF_SIZE)

    # 파일 내용 전송
    while data:
        sock.sendto(data, addr)
        data = f.read(BUF_SIZE)

    f.close()
