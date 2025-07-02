import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening on", HOST, PORT)

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = b""
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            data += chunk
        print("Received content:\n")
        print(data.decode('utf-8'))
