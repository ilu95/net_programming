from socket import *
import random

port = 9999
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
        if 'Hello' not in data:
            break

        sender = random.randrange(1, 50000)
        receiver = random.randrange(1, 50000)
        lumi = random.randrange(1, 100)
        humi = random.randrange(0, 100)
        temp = random.randrange(1, 100)
        air = random.randrange(1, 100)
        seq = random.randrange(1, 100000)
        text = f"{sender} {receiver} {lumi} {humi} {temp} {air} {seq}"
        conn.send(text.encode())
        conn.send(data)

    conn.close()
    print('Disconnected by', addr)
