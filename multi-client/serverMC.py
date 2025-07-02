import socket
import threading

# Define the host and port for the server
HOST = '127.0.0.1'  # Listen on all available interfaces
PORT = 12345        # Arbitrary non-privileged port

# List to keep track of all client connections
clients = []

# Broadcast a message to all connected clients except the sender
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

# Handle communication with a client
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Received: {message.decode()}")
                broadcast(message, client_socket)
            else:
                break
        except:
            break

    # Close the client connection when done
    clients.remove(client_socket)
    client_socket.close()

# Set up the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)  # Only accept 2 clients

    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Client {client_address} connected.")

        clients.append(client_socket)

        # Start a new thread to handle each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# Start the server
if __name__ == "__main__":
    start_server()
