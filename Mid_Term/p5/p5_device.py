from socket import *
import random

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 8888))
sock.listen(10)
print('Device is running')


while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE).decode()
    temp = 0
    humid = 0
    lumi = 0

    if msg == 'quit':
        conn.send(b'quit')
        break
    elif msg == '1':
        temp = int(random.randrange(1, 50))
        temp = temp.to_bytes(4, 'big')
        text = f"{temp} {humid} {lumi}"
        print(text)
        conn.send(text.encode())
        conn.close()
    elif msg == '2':
        humid = int(random.randrange(1, 100))
        humid = humid.to_bytes(4, 'big')
        text = f"{temp} {humid} {lumi}"
        conn.send(text.encode())
        conn.close()
    elif msg == '3':
        lumi = int(random.randrange(1, 150))
        lumi = humid.to_bytes(4, 'big')
        text = f"{temp} {humid} {lumi}"
        conn.send(text.encode())
        conn.close()


conn.close()
