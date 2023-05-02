import socket
import time

port = 7777
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)  # Set timeout to 1 second

while True:
    msg = input('Enter a message: ')
    if msg == 'q':
        break

    for i in range(3):
        sock.sendto(msg.encode(), ('localhost', port))
        ping = time.time()

        try:
            data, addr = sock.recvfrom(BUFFSIZE)
            pong = time.time()
            RTT = pong-ping
            print('Success: (RTT: ', RTT, ')')
            break  # Exit loop if 'ack' received
        except socket.timeout:
            print('Timeout, retrying...')
            if i == 2:
                print('Fail')
                break
        time.sleep(1)  # Wait for 1 second before retrying
sock.close()
