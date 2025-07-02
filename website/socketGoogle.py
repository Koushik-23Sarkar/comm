import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with error %s" % (err))

port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
    print("IP address of google is %s" % (host_ip))
except socket.gaierror:
    print("There was an error resolving the host")
    sys.exit()

s.connect((host_ip, port))
print("The socket has successfully connected to google")
