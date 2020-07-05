import socket
s = socket.socket()
print('socket created')
s.bind(('192.168.1.6',7236))
s.listen(3)
print('waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with", addr,"message from a client--",name)
    while True:
        chat=input("enter your message-")
        c.send(bytes(chat,'utf-8'))
        name = c.recv(1024).decode()
        print("---------reply from other one---------\n",name)
   # c.close()
