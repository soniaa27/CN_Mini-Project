import socket
import ssl
import threading
import time

HOST = '127.0.0.1'
PORT = 5050

#  Receive messages
def receive(sock):
    while True:
        msg = sock.recv(1024).decode()
        if msg:
            receive_time = time.time()
            try:
                sent_time = float(msg.strip().split()[-1])
                latency = receive_time - sent_time

                readable_time = time.strftime("%H:%M:%S", time.localtime(sent_time))

                print(
                    msg.strip(),
                    f"| Sent at: {readable_time}",
                    f"| Latency: {latency:.4f}s"
                )

            except:
                print(msg.strip())

# 1. Create SSL context
context = ssl._create_unverified_context()

# 2. Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Wrap with SSL
secure_sock = context.wrap_socket(sock, server_hostname=HOST)

# 4. Connect to server
secure_sock.connect((HOST, PORT))

# 5. Start receiving thread
threading.Thread(target=receive, args=(secure_sock,), daemon=True).start()

# 6. Subscribe loop
while True:
    topic = input("Subscribe to topic: ")
    secure_sock.send(f"SUBSCRIBE {topic}".encode())