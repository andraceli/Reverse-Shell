import socket

# Create socket object
s = socket.socket()

port = 4444
s.bind(('',port))
s.listen(5)

while True:
    c, addr = s.accept()
    c.send(b'Message from server\n')
    c.send(b'Welcome to this....\n')
    c.send(b'Programmer\n')
    
    c.close()
    break
