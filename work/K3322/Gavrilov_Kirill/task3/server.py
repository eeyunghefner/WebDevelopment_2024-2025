import socket
import sys

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(5)

conn, addr = sock.accept()

path = sys.path[0] + '/index.html'
headers = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'

inp = conn.recv(1024).decode()
print(inp)
with open(path, 'r', encoding='utf-8') as file:
    data = headers.encode() + ''.join(file.readlines()).encode()
    conn.send(data)

conn.close()


