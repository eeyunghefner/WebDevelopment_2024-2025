import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

print('Доступные формулы вычисления площади параллелограмма:\n'
      'Сторона параллелограмма * высота, проведенная к этой стороне\n'
      'Произведение смежных сторон параллелограмма на синус угла между ними (ввести угол в градусах)')
data = input().encode()

sock.send(data)

res = sock.recv(1024)
print(res.decode())

sock.close()


