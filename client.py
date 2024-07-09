import clipboard
import socket


#server_IP = int(input("Enter the Server IP | : "))
#server_port = int(input("Enter the Server port | : "))
server_IP = 'localhost'
server_port = 12345
received_content = ""
server_messagee = ""
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((server_IP,server_port))


def receive_mesage() :
    server_message = client_socket.recv(1024).decode('utf-8')

# while True:
server_messagee = client_socket.recv(1024).decode('utf-8')
client_socket.close()

clipboard.copy(server_messagee)
print("New clipboard content:", clipboard.paste())
