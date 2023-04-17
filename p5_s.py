import socket

# 서버 주소와 포트 번호
server_address = ('localhost', 10000)

# 소켓 생성 및 바인드
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

# 메시지 박스 딕셔너리 초기화
message_boxes = {}

while True:
    # 클라이언트로부터 메시지 수신
    data, address = sock.recvfrom(4096)

    # 수신한 데이터 디코딩 및 출력
    message = data.decode('utf-8')
    print(f'Received {message} from {address}')

    # 메시지 분석
    tokens = message.split(' ')
    if tokens[0] == 'send':
        # 메시지 박스에 메시지 저장
        mbox_id = tokens[1]
        msg = ' '.join(tokens[2:])
        if mbox_id not in message_boxes:
            message_boxes[mbox_id] = []
        message_boxes[mbox_id].append(msg)
        # 클라이언트에게 OK 전송
        response = 'OK'
        sock.sendto(response.encode('utf-8'), address)
    elif tokens[0] == 'receive':
        mbox_id = tokens[1]
        if mbox_id in message_boxes and len(message_boxes[mbox_id]) > 0:
            # 메시지 박스에서 제일 앞에 있는 메시지 전송 및 삭제
            msg = message_boxes[mbox_id].pop(0)
            sock.sendto(msg.encode('utf-8'), address)
        else:
            # 해당 mboxID에 메시지가 없는 경우 클라이언트에게 No messages 전송
            response = 'No messages'
            sock.sendto(response.encode('utf-8'), address)
    elif tokens[0] == 'quit':
        # 클라이언트에서 quit을 전송한 경우 루프 종료
        break

# 소켓 닫기
sock.close()
