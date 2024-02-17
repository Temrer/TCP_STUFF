import socket

HOST = "127.0.0.1"
PORT = 20048
ContinueCondition = True
response = None

def Main(s):
	while ContinueCondition:
		usrInput = bytes(input("> "), "utf-8")
		if usrInput == b"exit":
			return
		s.sendall(usrInput)
		global response
		response = s.recv(1024)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	Main(s)

print(f"received {response}")

