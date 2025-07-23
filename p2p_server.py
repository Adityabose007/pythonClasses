import socket
import threading

def receive_messages(conn):
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                print(f"Peer: {message}")
        except:
            print("Connection closed.")
            break

def send_messages(conn):
    while True:
        msg = input("You: ")
        conn.send(msg.encode())

def start_server():
    host = '0.0.0.0'  # Accept connections from any IP
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Waiting for a peer to connect...")
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
    send_messages(conn)

if __name__ == "__main__":
    start_server()
