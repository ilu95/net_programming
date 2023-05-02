from socket import *
import sys
import os

BUF_SIZE = 1024
LENGTH = 4  # '파일 크기': 4바이트

s = socket(AF_INET, SOCK_DGRAM)
s.settimeout(3)  # 타임아웃 설정

filename = input('Enter a filename: ')

# 파일 이름 전송
s.sendto(filename.encode(), ('localhost', 7777))

try:
    filesize, _ = s.recvfrom(BUF_SIZE)  # 파일 크기 수신
except timeout:
    print('Connection timeout')
    s.close()
    sys.exit()

if filesize == b'Nofile':
    print('No such file on the server')
    s.close()
    sys.exit()

filesize = int.from_bytes(filesize, 'big')
print('server:', filesize)  # 4바이트

rx_size = 0
f = open(filename, 'wb')

# 실제 파일 수신
while rx_size < filesize:
    try:
        data, _ = s.recvfrom(BUF_SIZE)
    except timeout:
        print('Connection timeout')
        s.close()
        sys.exit()
    f.write(data)
    rx_size += len(data)

print('Download complete')
s.close()
f.close()
