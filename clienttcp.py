import socket
import datetime

HOST = '192.168.1.11'
PORT = 48666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = s.recv(1024)
print('received: ' + str(data))
s.close()