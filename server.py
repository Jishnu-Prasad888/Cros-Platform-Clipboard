import socket

client_IP = 'localhost'
client_port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((client_IP,client_port))
server_socket.listen(5)
print(f"[*] Listening on {client_IP}:{client_port}")

client_socket, client_address = server_socket.accept()
print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

# while True:
message = "Hello world"
client_socket.send(message.encode('utf-8'))
client_socket.close()
server_socket.close()