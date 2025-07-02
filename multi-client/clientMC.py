import socket
import threading

# Define the server IP and port
SERVER_IP = '127.0.0.1'  # Replace with the server's IP address
PORT = 12345             # Same port as the server

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"\nNew message: {message.decode()}")
            else:
                break
        except:
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input("You: ")
        if message:
            client_socket.send(message.encode())

# Set up the client connection to the server
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    print("Connected to server...")

    # Start the thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Start the function to send messages
    send_messages(client_socket)

# Start the client
if __name__ == "__main__":
    start_client()
