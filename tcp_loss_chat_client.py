from socket import *
import time

port = 3333
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

while True:
    msg = input('-> ')

    # 메시지 송신
    sock.send(msg.encode())

    # 송신 메시지에 대한 응답 수신
    try:
        sock.settimeout(2)  # 2초간 대기 후 응답이 없으면 timeout 예외 발생
        data = sock.recv(BUFFSIZE)
    except timeout:
        print('[!] Response timeout')
        continue

    # 응답 수신 확인
    if data == b'ack':
        print('<- ', data.decode())
        break

    # 응답이 없을 경우 메시지 재송신
    else:
        print('[!] Response not received, resending message')
        continue

# 메시지 송신 및 수신
reTx = 0
while reTx <= 5:
    # 메시지 송신
    resp = str(reTx) + ' ' + msg
    sock.send(resp.encode())

    # 송신 메시지에 대한 응답 수신
    try:
        sock.settimeout(2)  # 2초간 대기 후 응답이 없으면 timeout 예외 발생
        data = sock.recv(BUFFSIZE)
    except timeout:
        print('[!] Response timeout')
        reTx += 1
        continue

    # 응답 수신 확인
    if data.decode() == 'ack':
        print('<- ', data.decode())
        break

    # 응답이 없을 경우 메시지 재송신
    else:
        print('[!] Response not received, resending message')
        reTx += 1
        continue

# 소켓 닫기
sock.close()
