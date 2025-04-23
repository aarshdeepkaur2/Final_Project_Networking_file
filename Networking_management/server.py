import socket
import os

HOST = '0.0.0.0' 
PORT = 5000
ALLOWED_DIR = os.getcwd()  # or set a safe directory like "./files"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[*] Listening on {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")

    filename = client_socket.recv(1024).decode()

    # Prevent directory traversal
    safe_path = os.path.abspath(os.path.join(ALLOWED_DIR, filename))
    if not safe_path.startswith(ALLOWED_DIR):
        client_socket.send(b'Access denied.')
        client_socket.close()
        continue
    
    if os.path.exists(safe_path):
        with open(safe_path, 'rb') as f:
            data = f.read()
            client_socket.sendall(data)
    else:
        client_socket.send(b'File not found.')

    client_socket.close()
