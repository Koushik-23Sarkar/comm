# Import socket module
import socket

# In this line we define our local host address with port number
SERVER = "127.0.0.1"
PORT = 8080

# Making a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client.connect((SERVER, PORT))

# Running an infinite loop
while True:
    print("Example : 4 + 5")
    # here we get the input from the user in the form operand operator operand
    inp = input("Enter the operation in the form operand operator operand: ")
    
    # If user wants to terminate the server connection he can type Over
    if inp == "Over":
        break

    # Here we send the user input to server socket by send method
    client.send(inp.encode())

    # Here we received output from the server socket
    answer = client.recv(1024)
    print("Answer is " + answer.decode())
    print("Type 'Over' to terminate")

client.close()
