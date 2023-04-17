import socket

HOST = '127.0.0.1'  # 호스트 IP
PORT = 9999        # 포트번호

# 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print('서버 실행 중...')

# 메시지를 저장할 딕셔너리 생성
message_boxes = {}

while True:
    # 클라이언트로부터 연결 요청이 오면 새로운 소켓 객체와 클라이언트의 주소 정보를 받음
    conn, addr = s.accept()
    print(f'클라이언트 [{addr}]가 연결되었습니다.')

    while True:
        # 클라이언트로부터 메시지를 수신
        data = conn.recv(1024)
        if not data:
            break

        # 수신한 데이터를 문자열로 변환 후 명령어와 인자로 분리
        message = data.decode()
        command = message.split()[0]
        mbox_id = message.split()[1]

        # 명령어에 따라 처리
        if command == 'send':
            # 해당 mbox_id에 메시지 저장 후 응답 전송
            message = ' '.join(message.split()[2:])
            if mbox_id in message_boxes:
                message_boxes[mbox_id].append(message)
            else:
                message_boxes[mbox_id] = [message]
            response = 'OK'
            conn.sendall(response.encode())
        elif command == 'receive':
            # 해당 mbox_id의 제일 앞에 있는 메시지를 전송 후 삭제
            if mbox_id in message_boxes and message_boxes[mbox_id]:
                message = message_boxes[mbox_id][0]
                message_boxes[mbox_id] = message_boxes[mbox_id][1:]
                conn.sendall(message.encode())
            else:
                response = 'No messages'  # 메시지가 없는 경우
                conn.sendall(response.encode())
        elif command == 'quit':
            # 클라이언트와 연결 종료
            conn.close()
            print(f'클라이언트 [{addr}]와 연결이 종료되었습니다.')
            break
        else:
            # 잘못된 명령어인 경우
            response = 'Invalid command'
            conn.sendall(response.encode())
