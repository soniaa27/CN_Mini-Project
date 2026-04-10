import threading
import socket
import ssl
import time

HOST = '127.0.0.1'
PORT = 5050

def create_client():
    context = ssl._create_unverified_context()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_sock = context.wrap_socket(sock, server_hostname=HOST)

    secure_sock.connect((HOST, PORT))
    secure_sock.send(b"SUBSCRIBE sports")

    #  KEEP CLIENT ALIVE
    while True:
        time.sleep(10)

for _ in range(30):
    threading.Thread(target=create_client).start()