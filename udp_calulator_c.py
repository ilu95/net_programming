import socket

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('UDP Calculator Client started')

while True:
    message = input("Enter an expression (e.g. 20 + 17) or 'q' to quit: ")
    sock.sendto(message.encode(), (HOST, PORT))
    if message == 'q':
        break
    data, addr = sock.recvfrom(BUFSIZE)
    result = data.decode()
    print(f"Result: {result}")

sock.close()
