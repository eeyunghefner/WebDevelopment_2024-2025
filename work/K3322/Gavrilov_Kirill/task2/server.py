import socket
from math import sin, pi

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()

conn, addr = sock.accept()

data = conn.recv(1024).decode()
params = list(map(float, data.split()))

if len(params) == 2:
    res = str(params[0] * params[1]).encode()
elif len(params) == 3:
    res = str(params[0] * params[1] * sin(params[2] * pi / 180)).encode()
else:
    res = b'Invalid params'

conn.send(res)

conn.close()


