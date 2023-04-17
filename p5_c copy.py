import socket

HOST = '127.0.0.1'  # 서버의 호스트 IP
PORT = 9999        # 서버의 포트번호

# 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # 사용자로부터 명령어 입력받기
    message = input(
        'Enter the message("send mboxId message" or "receive mboxId"): ')

    # 서버로 메시지 전송
    s.sendall(message.encode())

    # 서버로부터 응답 수신
    response = s.recv(1024).decode()

    # 응답 출력
    print(response)

    if message == 'quit':
        # 프로그램 종료
        s.close()
        break
