from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)
print('Server started')

while True:
    conn, addr = sock.accept()
    print('Connected by', addr)

    # 클라이언트와의 통신
    while True:
        data = conn.recv(BUFFSIZE)
        if not data:
            break

        # 수신한 데이터를 그대로 클라이언트에게 전송
        conn.send(data)

    conn.close()
    print('Disconnected by', addr)
