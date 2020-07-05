import socket
c = socket.socket()
c.connect(('localhost',9999))
while True:
    name = input("enter your message-")
    c.send(bytes(name,'utf-8'))
    print("---------reply from other one---------\n",c.recv(1024).decode())
