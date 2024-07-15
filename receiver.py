import socket
import pyperclip

# Server configuration
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12345

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(1)
        print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")
        
        client_socket, client_addr = server_socket.accept()
        print(f"[*] Accepted connection from {client_addr[0]}:{client_addr[1]}")
        
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"[+] Received clipboard content from client: {data}")
            pyperclip.copy(data)  # Update server's clipboard with received content
            
        client_socket.close()

if __name__ == '__main__':
    start_server()
