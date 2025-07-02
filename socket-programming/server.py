import socket

host = "127.0.0.1"
port = 5002

server = socket.socket()
server.bind((host, port))
server.listen()

conn, addr = server.accept()
print("Connection from: " + str(addr))

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    data = str(data).upper()
    print("From client: " + str(data))
    data = input("Type message: ")
    conn.send(data.encode())

conn.close()
