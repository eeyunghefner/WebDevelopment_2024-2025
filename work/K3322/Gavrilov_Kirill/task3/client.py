import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

sock.send(b'Hello, server')

res = sock.recv(1024).decode()
print(res)

sock.close()
