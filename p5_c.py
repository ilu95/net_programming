import socket

# 서버 주소와 포트 번호
server_address = ('localhost', 10000)

# 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 사용자로부터 메시지 입력 받기
    message = input(
        'Enter the message("send mboxId message" or "receive mboxId"): ')

    # 서버로 메시지 전송
    sock.sendto(message.encode('utf-8'), server_address)

    # 서버로부터 응답 수신
    data, address = sock.recvfrom(4096)

    # 수신한 데이터 디코딩 및 출력
    response = data.decode('utf-8')
    print(response)

    # quit 입력 시 루프 종료
    if message == 'quit':
        break

# 소켓 닫기
sock.close()
