import time
import socket
import pyperclip

client_IP = 'localhost'
client_port = 12345
boolean = True
current_clipboard = pyperclip.paste()
old_clipboard = ''

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((client_IP,client_port))
server_socket.listen(5)
print(f"[*] Listening on {client_IP}:{client_port}")

client_socket, client_address = server_socket.accept()
print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

while boolean:
    if current_clipboard != old_clipboard and current_clipboard != '' :
        client_socket.send(current_clipboard.encode('utf-8'))
        old_clipboard = current_clipboard
        time.sleep(1)
    current_clipboard = pyperclip.paste()

client_socket.close()
server_socket.close()