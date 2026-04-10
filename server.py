import socket
import threading
import ssl

HOST = '0.0.0.0'
PORT = 5050

# topic -> set of subscriber sockets
subscriptions = {}
lock = threading.Lock()

client_count = 0


def handle_client(conn, addr):
    global subscriptions

    print(f"[CONNECTED CLIENT THREAD] {addr}")

    try:
        while True:
            msg = conn.recv(1024).decode()

            if not msg:
                break

            parts = msg.split(" ", 2)
            command = parts[0]

            #  SUBSCRIBE
            if command == "SUBSCRIBE":
                topic = parts[1]

                with lock:
                    subscriptions.setdefault(topic, set()).add(conn)

                conn.send(f"Subscribed to {topic}\n".encode())

            #  PUBLISH
            elif command == "PUBLISH":
                topic = parts[1]
                message = parts[2]

                with lock:
                    if topic in subscriptions:
                        for sub in subscriptions[topic].copy():
                            try:
                                sub.send(f"[{topic}] {message}\n".encode())
                            except:
                                subscriptions[topic].discard(sub)
                                print("Removed disconnected client")

            # 🔹 UNSUBSCRIBE
            elif command == "UNSUBSCRIBE":
                topic = parts[1]

                with lock:
                    if topic in subscriptions:
                        subscriptions[topic].discard(conn)

                conn.send(f"Unsubscribed from {topic}\n".encode())

            # 🔹 INVALID COMMAND
            else:
                conn.send(b"Invalid command\n")

    except Exception as e:
        print(f"[ERROR] {addr} -> {e}")

    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr}")


def start_server():
    global client_count

    # 🔐 SSL setup
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    # 🔌 Create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 🔧 Optimization: reuse port
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    with context.wrap_socket(server, server_side=True) as secure_server:
        print("[SERVER RUNNING]")

        while True:
            conn, addr = secure_server.accept()

            client_count += 1
            print(f"[CONNECTED] {addr} | Total clients: {client_count}")

            thread = threading.Thread(
                target=handle_client,
                args=(conn, addr),
                daemon=True
            )
            thread.start()


if __name__ == "__main__":
    start_server()