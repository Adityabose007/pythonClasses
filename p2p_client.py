import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if message:
                print(f"Peer: {message}")
        except:
            print("Connection closed.")
            break

def send_messages(sock):
    while True:
        msg = input("You: ")
        sock.send(msg.encode())

def start_client():
    host = input("Enter peer IP (e.g. 127.0.0.1): ")
    port = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("Connected to peer.")

    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()
    send_messages(sock)

if __name__ == "__main__":
    start_client()
