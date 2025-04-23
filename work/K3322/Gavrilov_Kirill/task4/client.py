import socket
import threading


def get_message(sock):
    while True:
        message = sock.recv(1024)
        if not message:
            break
        print(message.decode())


def send_message(sock):
    while True:
        message = input()
        if message == 'exit':
            sock.send('exit'.encode())
            break
        else:
            sock.send(message.encode())


client = socket.socket()
client.connect(('localhost', 9090))

client_name = input("Enter your name: ")
client.send(client_name.encode())

get_thread = threading.Thread(target=get_message, args=(client,))
get_thread.start()

send_thread = threading.Thread(target=send_message, args=(client,))
send_thread.start()
