import socket
import os
import pymysql
import requests  # Safer alternative
from urllib.parse import urlparse

HOST = '127.0.0.1'
PORT = 5000

filename = input("Enter the filename to download: ") 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send(filename.encode())  

data = client.recv(409600)
with open(filename, 'wb') as f:
    f.write(data)

def get_data():
    url = 'https://insecure-api.com/get-data'
    
    # Validate the URL scheme
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        raise ValueError("Unsupported URL scheme.")
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

print("[+] File received.")
client.close()
