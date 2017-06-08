import socket

host = '78.28.44.214'
port = 12344

s = socket.socket()

while True:
    s = socket.socket()
    s.connect((host, port))
    print(str(s.recv(1024))[2:-1].replace('\\n', '\n'))
    print("Send:")
    reply = input("$ ").encode()
    s.send(reply)
    print(str(s.recv(4096))[2:-1].replace('\\n', '\n'))
    s.close()