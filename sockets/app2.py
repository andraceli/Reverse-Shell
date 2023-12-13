import socket

s = socket.socket()
port = 4444

s.connect(('192.168.8.101', port))

print(s.recv(1024).decode())
s.close()
