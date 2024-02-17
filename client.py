import socket

HOST = "192.168.0.1"
PORT = "20048"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b"HELLO WORLD")
	data = s.recv(1024)

pritn(f"received {data!r}")

