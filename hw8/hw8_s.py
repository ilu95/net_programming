import socket
import threading
import time

# 클라이언트 목록
clients = []

# 클라이언트와 통신하는 스레드 함수
def client_handler(conn, addr):
    global clients

    # 새로운 클라이언트이면 목록에 추가
    if addr not in clients:
        print('new client', addr)
        clients.append(conn)

    while True:
        try:
            # 클라이언트로부터 데이터 수신
            data = conn.recv(1024)
            if not data:
                break
            print(time.asctime() + str(addr) + ':' + data.decode())

            # 수신한 데이터를 현재 연결된 모든 클라이언트에게 전송
            for client in clients:
                if client != conn:
                    client.send(data)
        except ConnectionResetError:
            # 클라이언트와 연결이 끊어짐
            break

    # 클라이언트 소켓을 목록에서 제거
    clients.remove(conn)
    conn.close()




# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 2500))
server_socket.listen()

print('Server Started')

while True:
    # 클라이언트 연결 대기
    conn, addr = server_socket.accept()
    
    # 클라이언트와 통신하는 스레드 생성
    th = threading.Thread(target=client_handler, args=(conn, addr))
    th.daemon = True
    th.start()
