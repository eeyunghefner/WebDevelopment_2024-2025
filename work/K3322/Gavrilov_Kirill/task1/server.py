import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()

conn, addr = sock.accept()
# print(f'{conn} \n {addr}')

data = conn.recv(1024)
if data == b'Hello, server':
    print(data.decode())
    conn.send(b'Hello, client')
else:
    print('Another data')
    conn.send(b'Who you are?')

conn.close()


