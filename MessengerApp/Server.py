import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockpt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

clients = {}


def recieve_messsage(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(
        sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = recieve_messsage(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user

            print(f"Accepted new connection from {client_address[0]}:{
                  client_address[1]} username: {user["data"].decode("utf-8")}")

        else:
            messsage = recieve_messsage(notified_socket)

            if message is false:
                print(f"Closed connection from {client})
