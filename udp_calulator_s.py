import socket

HOST = ''
PORT = 5000
BUFSIZE = 1024


def calculate(expression):
    try:
        operator_index = expression.find(' ')
        operand1 = int(expression[:operator_index])
        operator = expression[operator_index+1]
        operand2 = int(expression[operator_index+3:])
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            result = round(operand1 / operand2, 1)
        else:
            raise Exception('Invalid operator')
        return str(result)
    except:
        return 'Error: Invalid expression'


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print('UDP Calculator Server started')

while True:
    data, addr = sock.recvfrom(BUFSIZE)
    message = data.decode()
    if message == 'q':
        break
    result = calculate(message)
    sock.sendto(result.encode(), addr)

sock.close()
