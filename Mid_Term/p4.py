from socket import *
sock = socket(AF_INET, SOCK_STREAM)
ip = '220.69.189.125'
port = 443

sock.connect((ip, port))
sock.send(b'GET / HTTP/1.1\r\n\r\n')
data = sock.recv(10000)
print(data.decode())
sock.close()
