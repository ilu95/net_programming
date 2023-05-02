from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    try:
        data, addr = sock.recvfrom(BUFSIZE)
        print('connected by', addr[0], addr[1])
    except:
        break
    else:
        print("Received message: ", data.decode())
        try:
            sock.sendto(data, addr)
        except:
            break

sock.close()
