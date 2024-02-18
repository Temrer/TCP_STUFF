import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 20048  # Port to listen on (non-privileged ports are > 1023)

def handleConnection(conn_data):
	conn, addr = conn_data[0], conn_data[1]
	print(f"connection has been established at address {addr[0]}, port {addr[1]}")
	userNotExited = True
	while userNotExited:
		data = conn.recv(1024)
		print(data)
		if not data:
			print("user exited")
			conn.close()
			return

		conn.sendall(data)


def runLobby():
	continueCondition = True
	backgroundTasks = set()
	while continueCondition:
		print("awaiting connection")
		conn, addr = s.accept()
		print("connection incoming", addr)
		thread_handleConnection = threading.Thread(target=handleConnection, args={(conn, addr)})
		thread_handleConnection.start()
		


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	print("initializing server")
	runLobby()

