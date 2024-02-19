import socket
import threading
import Utils.Parser as Parser




HOST = "127.0.0.1"
PORT = 20048

try:
	with open("ServerAddress.txt", "r") as source:
		HOST, PORT = Parser.processAddressInfo(source) 
except FileNotFoundError as e:
	print("No Addres information specified. Trying to connect to localhost...")


print(HOST,PORT)
ContinueCondition = True
response = None
message_target = "all"

def Main(s):
	global ContinueCondition
	while ContinueCondition:
		global message_target
		usrInput = input()
		if usrInput == "exit":
			s.close()
			ContinueCondition = False
			return
		
		words = usrInput.split(" ")
		if words[0] == "/w":
			message_target = words[1]
		
		msg = f"({message_target}): {usrInput}"
		processedMessage = bytes(msg, "utf-8")
		s.sendall(processedMessage)


def Listen(s):
	global ContinueCondition
	while ContinueCondition:
		response = s.recv(1024)
		msg = response.decode("utf-8")
		print(f"<< {msg}")



s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
thread_Main = threading.Thread(target=Main, args={s})
thread_Listen = threading.Thread(target=Listen, args ={s})
thread_Main.start()
thread_Listen.start()



