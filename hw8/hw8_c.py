import socket
import threading

# 서버 주소와 포트
server_addr = ('localhost', 2500)

# 소켓 생성 및 서버에 접속
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addr)

# ID 입력
my_id = input('ID를 입력하세요: ')
sock.send(f'[ {my_id} ]'.encode())

# 클라이언트 송신 스레드 함수
def send_msg():
    while True:
        msg = '[' + my_id + '] ' + input()
        sock.send(msg.encode())

# 클라이언트 송신 스레드 생성
th = threading.Thread(target=send_msg)
th.daemon = True
th.start()

# 서버에서 보내는 데이터 수신 및 출력
while True:
    try:
        data = sock.recv(1024)
        if not data:
            break
        print(data.decode())
    except:
        break

sock.close()
