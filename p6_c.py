import socket
import time

port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1.0)  # Set timeout to 1 second

while True:
    msg = input('Enter a message: ')
    if msg == 'q':
        break

    # Send message up to 4 times in case of packet loss
    for i in range(4):
        sock.sendto(msg.encode(), ('localhost', port))

        try:
            data, addr = sock.recvfrom(BUFFSIZE)
            print('Server says: ', data.decode())
            break  # Exit loop if 'ack' received
        except socket.timeout:
            print('Timeout, retrying...')
            if i == 3:
                print('Max retry exceeded')
                break
        time.sleep(1)  # Wait for 1 second before retrying
sock.close()
