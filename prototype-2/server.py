import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break

        # Implement your message routing logic here
        # For demonstration purposes, we'll simply print the received message
        print(f"Received message from client: {data.decode('utf-8')}")

    # Close the client socket when the client disconnects
    client_socket.close()

def start_server():
    # Set up the server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8888))
    server.listen(5)
    print("[INFO] Server listening on port 8888...")

    while True:
        # Wait for a client to connect
        client, addr = server.accept()
        print(f"[INFO] Accepted connection from {addr[0]}:{addr[1]}")

        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
