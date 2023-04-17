import socket

HOST = 'localhost'
PORT = 9000
EXTERNAL_HOST = 'www.daum.net'
EXTERNAL_PORT = 80


def relay_server():
    # 소켓 생성
    browser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    external_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 소켓 바인드 및 리스닝
    browser_socket.bind((HOST, PORT))
    browser_socket.listen()

    # 브라우저 연결 수신 및 외부 서버 연결
    while True:
        conn, addr = browser_socket.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            if not data:
                break

            # HTTP 요청 메시지에서 요청 라인과 Host 헤더 추출
            request_line, headers = data.decode().split('\r\n', 1)
            host_header = 'Host: ' + EXTERNAL_HOST
            headers = headers.replace('Host: localhost:9000', host_header)

            # 외부 서버 연결
            external_socket.connect((EXTERNAL_HOST, EXTERNAL_PORT))
            external_socket.sendall((request_line + '\r\n' + headers).encode())

            # 외부 서버로부터 HTTP 응답 수신 후 브라우저에게 전달
            while True:
                response = external_socket.recv(1024)
                if not response:
                    break
                conn.sendall(response)

            # 연결 종료
            external_socket.close()
            conn.close()


if __name__ == '__main__':
    relay_server()
