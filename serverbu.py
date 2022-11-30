import socket

def send_text(sending_socket, text):
    text = text + "\n"
    data = text.encode()
    sending_socket.send(data)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen()
print("Waiting for connection")
connection_socket, address = server_socket.accept()
print("Client connected")

message = "Hello, thanks for connecting"
# data = message.encode()
# connection_socket.send(data)
send_text(connection_socket, message)

connection_socket.close()
server_socket.close()