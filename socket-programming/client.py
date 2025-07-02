import socket

host = "127.0.0.1"
port = 5002

obj = socket.socket()
obj.connect((host, port))

message = input("Type message: ")
while message != 'q':
    obj.send(message.encode())
    data = obj.recv(1024).decode()
    print("Received from server: " + data)
    message = input("Type message: ")

obj.close()
