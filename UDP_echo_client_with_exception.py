import socket

port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Message to send: ")
    try:
        bytesSent = s.sendto(msg.encode(), address)
    except:
        print('connection closed')
        break
    else:
        print("{} bytes send".format(bytesSent))
        try:
            data, addr = s.recvfrom(BUFSIZE)
        except:
            print('connection closed')
            break
        else:
            if not data:
                break
            print("Received message: %s" % data.decode())

s.close()
