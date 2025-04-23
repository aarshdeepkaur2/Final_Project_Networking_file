import socket
import os

HOST = '0.0.0.0' 
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[*] Listening on {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")

   
    filename = client_socket.recv(1024).decode()
    
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            data = f.read()
            client_socket.sendall(data)
    else:
        client_socket.send(b'File not found.')

    client_socket.close()
