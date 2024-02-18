def parseMsg(msg):
	message_parts = msg.split(":")
	target 	= message_parts[0][1:-1]
	txt		= message_parts[1]

	return target, txt



