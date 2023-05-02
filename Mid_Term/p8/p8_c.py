import socket

# 서버 주소와 포트 번호
server_address = ('localhost', 10000)

# 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(10):
    time = 2
    # 사용자로부터 메시지 입력 받기
    message = input(
        'Enter the message("send mboxId message" or "receive mboxId"): ')
    while True:
        # 서버로 메시지 전송
        sock.sendto(message.encode('utf-8'), server_address)
        sock.settimeout(time)

        try:
            # 서버로부터 응답 수신
            data, address = sock.recvfrom(4096)
        except TimeoutError:
            time += 2
            if time > 6:
                break
        else:
            # 수신한 데이터 디코딩 및 출력
            response = data.decode('utf-8')
            print(response)
            break

        # quit 입력 시 루프 종료
        if message == 'quit':
            break
