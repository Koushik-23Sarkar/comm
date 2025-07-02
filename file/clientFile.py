import socket

HOST = '127.0.0.1'  # Server IP
PORT = 65432        # Server Port

file_path = 'tcp_connection_data.txt'  # Text file to send

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open(file_path, 'r') as file:
        content = file.read()
        s.sendall(content.encode('utf-8'))
    print("File sent to server.")
