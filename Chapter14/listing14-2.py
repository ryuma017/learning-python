import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print(str(s.recv(1024), "utf-8"))