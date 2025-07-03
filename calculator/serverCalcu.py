# server.py

import socket

# Server configuration
LOCALHOST = "127.0.0.1"
PORT = 8080

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)

print("Server started")
print("Waiting for client request...")

clientConnection, clientAddress = server.accept()
print("Connected client:", clientAddress)

while True:
    data = clientConnection.recv(1024)
    msg = data.decode()

    if msg.lower() == "over":
        print("Connection is Over")
        break
    print("Equation is received")
    print("Received equation:", msg)
    result = 0
    operation_list = msg.strip().split()

    # Validate format: should be exactly 3 parts
    if len(operation_list) != 3:
        error_msg = "Error: Input must be in the format 'operand1 operator operand2'"
        clientConnection.send(error_msg.encode())
        continue

    oprnd1, operator, oprnd2 = operation_list

    try:
        num1 = float(oprnd1)
        num2 = float(oprnd2)

        if operator == "+":
            result = num1 + num2
            print("Send the result to client")
        elif operator == "-":
            result = num1 - num2
            print("Send the result to client")
        elif operator == "*":
            result = num1 * num2
            print("Send the result to client")
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
            print("Send the result to client")
        else:
            raise ValueError("Unsupported operator")

        clientConnection.send(str(result).encode())

    except ValueError:
        clientConnection.send("Error: Invalid number or operator.".encode())
    except ZeroDivisionError:
        clientConnection.send("Error: Cannot divide by zero.".encode())

clientConnection.close()