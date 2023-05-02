from socket import *
import threading

port = 3333
BUFFSIZE = 1024

# 클라이언트와 통신하는 스레드


def client_thread(conn, addr):
    # 연결된 클라이언트의 주소 출력
    print('Connected by', addr)

    # 초기 연결 메시지 송신
    conn.send(b'ack')

    # 클라이언트와 통신하는 루프
    while True:
        try:
            data = conn.recv(BUFFSIZE)
        except:
            print('Connection closed')
            break

        # 클라이언트로부터 메시지 수신
        if not data:
            print('Connection closed')
            break

        # 수신한 메시지 출력
        print('<-', data.decode())

        # 메시지 송신
        conn.send(b'ack')

    # 클라이언트와 연결 종료
    conn.close()
    print('Disconnected by', addr)


# 소켓 생성 및 바인딩
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)
print('Server started...')

# 클라이언트 연결을 받는 루프
while True:
    conn, addr = sock.accept()
    # 새로운 스레드 생성하여 클라이언트와 통신
    t = threading.Thread(target=client_thread, args=(conn, addr))
    t.start()
