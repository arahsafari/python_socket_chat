import socket
import datetime

HOST = ''
PORT = 48666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print('listen to ip {} port {}'.format(HOST, PORT))

while True:
    conn, addr = s.accept()
    dt = datetime.datetime.now()
    message = raw_input('Please keyin the message you want to send!')
    conn.send(message.encode())
    print('message', message)
    conn.close()