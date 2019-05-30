import socket
host = "127.0.0.1"
port = 9000
#create a server side socket
s = socket.socket()
s.bind((host, port))
s.listen(5)
c, addr = s.accept()
print("A client connected: ")
while True:
	data = c.recv(1024)
	if not data:
		break
	print("from client: "+str(data.decode()))
	data1 = raw_input("enter response:")
	c.send(data1.encode())
c.close()
