import socket
import time

# 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 소켓 바인딩
s.bind(('localhost', 9999))

while True:
    # 클라이언트로부터 데이터 수신
    data, addr = s.recvfrom(1024)

    # 현재 시간 전송
    s.sendto(time.ctime(time.time()).encode(), addr)
