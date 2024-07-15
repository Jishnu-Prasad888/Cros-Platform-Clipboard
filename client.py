import clipboard
import socket
#server_IP = int(input("Enter the Server IP | : "))
#server_port = int(input("Enter the Server port | : "))
server_IP = 'localhost'
server_port = 12345
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((server_IP,server_port))

while True:
    server_messagee = client_socket.recv(1024).decode('utf-8')
    if server_messagee :
        clipboard.copy(server_messagee)
        print("New clipboard content:", clipboard.paste())

client_socket.close()