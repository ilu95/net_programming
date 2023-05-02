import socket

HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024


def calculate(expr):
    """수식을 계산하는 함수"""
    try:
        # eval 함수로 수식 계산 후, 결과값을 소수점 1자리까지 표시하고 문자열로 변환
        return str(round(eval(expr), 1))
    except:
        return "Error: invalid expression"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f'Server listening on {PORT}...')

    conn, addr = server_socket.accept()
    print(f'Connected by {addr}')

    with conn:
        while True:
            data = conn.recv(BUFSIZE)
            if not data:
                continue
            expr = data.decode().strip()  # 수신받은 데이터를 디코딩하고 양쪽 공백 제거
            print(f'Received expression: {expr}')

            if expr.lower() == 'q':
                break

            result = calculate(expr)
            print(f'Send result: {result}')
            conn.send(result.encode())
