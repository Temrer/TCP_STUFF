import socket
import threading
import asyncio

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 20048  # Port to listen on (non-privileged ports are > 1023)
thread_runLobby 

def handleConnection(conn, addr):
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
	global thread_runLobbby
	continueCondition = True
	backgroundTasks = set()
	while continueCondition:
		print("awaiting connection")
		conn, addr = s.accept()
		print("connection inclming", addr)
		#new_task = asyncio.to_thread(handleConnection(conn, addr))
		#backgroundTasks.add(new_task)
		thread_handleConnection = threading.Thread(target=handleConnection, args={conn, addr})
		thread_handleConnection.start()
		thread_handleConnection.join()
		thread_runLobby.join()
		


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	global thread_runLobby
	s.bind((HOST, PORT))
	s.listen()
	print("initializing server")
	thread_runLobby = threading.Thread(target=runLobby)
	thread_runLobby.start()
	thread_runLobby.join()

