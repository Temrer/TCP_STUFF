import socket
import asyncio

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 20048  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	print("initializing server")
	conn, addr = s.accept()
	with conn:
		print(f"Connected by {addr}")
		while True:
			data = conn.recv(1024)
			print(data)
			if not data:
				break
			conn.sendall(data)


