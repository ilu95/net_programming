import socket

HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        expr = input('Enter an arithmetic expression (q to quit): ')
        if expr.strip().lower() == 'q':
            client_socket.send(expr.encode())
            break
        client_socket.send(expr.encode())
        result = client_socket.recv(BUFSIZE)
        print(f'Result: {result.decode()}')
