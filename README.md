# Cros-Platform-Clipboard
-------------------

# Clipboard Sync Client

## Description
This Python script connects to a server and synchronizes the clipboard content. It continuously receives messages from the server and updates the local clipboard accordingly.

## Requirements
- Python 3.x
- `clipboard` library (install using `pip install clipboard`)

## Usage
1. Modify `server_IP` and `server_port` variables to match your server configuration.
2. Run the script.
3. Connects to the server specified by `server_IP` and `server_port`.
4. Copies the received message to the local clipboard whenever a new message is received from the server.
5. Prints the updated clipboard content to the console.

---------------

# Clipboard Sync Server

## Description
This Python script sets up a server that listens for incoming connections from clients. It receives clipboard content from clients and updates its own clipboard accordingly using the `pyperclip` library.

## Requirements
- Python 3.x
- `pyperclip` library (install using `pip install pyperclip`)

## Usage
1. Modify `SERVER_HOST` and `SERVER_PORT` variables to specify the server's IP address and port.
2. Run the script.
3. Waits for incoming connections from clients.
4. Upon connection, receives clipboard content from the client and updates the server's clipboard.
5. Prints the received clipboard content to the console.
