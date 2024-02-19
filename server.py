import socket
import threading
import Utils.Parser as Parser

HOST = "192.168.0.169"  # Standard loopback interface address (localhost)
PORT = 20048 # Port to listen on (non-privileged ports are > 1023)

Users = []


def Broadcast(usr_data, msg):
	global Users
	for conn_data in Users:
		if conn_data[1] != usr_data[1]:
			conn = conn_data[0]
			
			msg = f"{usr_data[2]}: {msg}"
			data = bytes(msg, "utf-8")
			conn.sendall(data)


def ProcessMessage(usr_data, msg):
	target, msg = Parser.parseMsg(msg)
	if target != "all":
		#do stuff
		return
	
	Broadcast(usr_data, msg)


def handleConnection(conn_data):
	conn, addr = conn_data[0], conn_data[1]
	conn.sendall(b"Choose a nickname")
	nickname = conn.recv(1024).decode("utf-8")
	_, nickname = Parser.parseMsg(nickname) 
	usr_data = (conn, addr, nickname)
	global Users
	Users.append(usr_data)
	print(f"connection has been established at address {addr[0]}, port {addr[1]}")
	userNotExited = True
	while userNotExited:
		data = conn.recv(1024)
		print(data)
		msg = data.decode("utf-8")
		if not data:
			print("user exited")
			conn.close()
			Users.remove(usr_data)
			return
		ProcessMessage(usr_data, msg)


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
