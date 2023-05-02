from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 80))

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    request_url = req[0].split()[1][1:]

    print(request_url)
    print()

    if request_url == 'index.html':
        f = open(request_url, 'r', encoding='utf-8')
        mimeType = 'text/html'
        s.sendto('HTTP/1.1 200 OK\r\n'.encode(), addr)
        s.sendto(('Content-Type: ' + mimeType + '\r\n').encode(), addr)
        s.sendto('\r\n'.encode(), addr)
        s.sendto(f.read().encode('euc-kr'), addr)

    elif request_url == 'iot.png':
        f = open(request_url, 'rb')
        mimeType = 'image/png'
        s.sendto('HTTP/1.1 200 OK\r\n'.encode(), addr)
        s.sendto(('Content-Type: ' + mimeType + '\r\n').encode(), addr)
        s.sendto('\r\n'.encode(), addr)
        s.sendto(f.read(), addr)

    elif request_url == 'favicon.ico':
        f = open(request_url, 'rb')
        mimeType = 'image/x-icon'
        s.sendto('HTTP/1.1 200 OK\r\n'.encode(), addr)
        s.sendto(('Content-Type: ' + mimeType + '\r\n').encode(), addr)
        s.sendto('\r\n'.encode(), addr)
        s.sendto(f.read(), addr)

    else:
        s.sendto('HTTP/1.1 404 Not Found\r\n'.encode(), addr)
        s.sendto('\r\n'.encode(), addr)
        s.sendto('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode(), addr)
        s.sendto('<BODY>NOT FOUND</BODY></HTML>'.encode(), addr)
