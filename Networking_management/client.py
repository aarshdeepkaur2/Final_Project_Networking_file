import socket
import os
import pymysql
from urllib.request import urlopen

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
    data = urlopen(url).read().decode()
    return data

print("[+] File received.")
client.close()
