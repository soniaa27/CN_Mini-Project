import socket
import ssl
import time

HOST = '127.0.0.1'
PORT = 5050

# 1. Create SSL context
context = ssl._create_unverified_context()

# 2. Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Wrap with SSL
secure_sock = context.wrap_socket(sock, server_hostname=HOST)

# 4. Connect to server
secure_sock.connect((HOST, PORT))

# 5. Send messages in loop
while True:
    topic = input("Topic: ")
    message = input("Message: ")

    timestamp = time.time()

    secure_sock.send(
        f"PUBLISH {topic} {message} {timestamp}".encode()
    )