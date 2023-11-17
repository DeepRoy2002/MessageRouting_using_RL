import socket
import time

def send_message(source, destination, message):
    # Set up the client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))  # Connect to the server

    # Send the message with source and destination information
    data = f"{source},{destination},{message}"
    client.send(data.encode('utf-8'))

    # Close the client socket
    client.close()

if __name__ == "__main__":
    # Example: Send a message from a machine to a server
    source_machine = 1
    destination_server = 9
    message_to_send = "Hello, Server! This is a test message."

    send_message(source_machine, destination_server, message_to_send)
