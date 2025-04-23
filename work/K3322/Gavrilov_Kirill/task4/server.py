import socket
import threading


def client_handler(sock, adr, name):
    print(f'New client: {name} {adr}')
    global has_had_connection
    has_had_connection = True
    while True:
        message = sock.recv(1024)
        if not message or message == b'exit':
            break
        message = message.decode()
        print(f'Message from {name}: "{message}"')
        for cli in clients:
            if cli != sock:
                cli.send(f'{name}: "{message}"'.encode())
    sock.close()
    print(f'Connection with client {name} {adr} has closed')
    clients.remove(sock)


server = socket.socket()
server.bind(('', 9090))
server.listen(5)

clients = list()
has_had_connection = False

while True:

    client_socket, address = server.accept()
    clients.append(client_socket)

    cli_name = client_socket.recv(1024).decode()

    client_thread = threading.Thread(target=client_handler, args=(client_socket, address, cli_name))
    client_thread.start()
