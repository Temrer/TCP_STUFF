def parseMsg(msg):
	message_parts = msg.split(":")
	target 	= message_parts[0][1:-1]
	txt		= message_parts[1]

	return target, txt

def processAddressInfo(info_file):
	ip_info=info_file.readline().split("=")
	port_info=info_file.readline().split("=")
	if ip_info[0] != "IP" or port_info[0] != "PORT" :
		raise ValueError("File format should be:\nIP=\"<ip addres>\"\nPORT=<port>"
	ip_addr = ip_info[1]
	ip_segments = ip_addr.split("\"")[1].split(".")
	print(ip_segments)
	if len(ip_segments)!=4:
		raise TypeError("Invalid ip address. Format should range from 00.00.00.00 to 255.255.255.255")
	for segment in ip_segments:
		try:
			a = int(segment)
		except Exception as _ :
			raise TypeError("Invalid ip address. Please use only integers")
		if a<0 or a>255:
			raise ValueError("Ip segments should range from 0 to 255")
	try:
		port = int(port_info[1])
	except Exception as _:
		raise TypeError("Invalid port. Port should be of type integer")


	return ip_addr, port

