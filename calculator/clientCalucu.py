# client.py

import socket

# Server details
SERVER = "127.0.0.1"
PORT = 8080

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

print("Connected to server.")
print("Type equations like: 4 + 5 or 10 / 2")
print("Type 'Over' to end the connection.\n")

while True:
    user_input = input("Enter operation: ")

    if user_input.lower() == "over":
        client.send(user_input.encode())
        break

    # Send to server
    client.send(user_input.encode())

    # Receive and print response
    result = client.recv(1024).decode()
    print("Result:", result)
    print()

client.close()