import socket

port = 80
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Request URL: ")
    s.sendto(msg.encode(), address)

    data, addr = s.recvfrom(BUFSIZE)
    msg = data.decode()
    print(msg)
