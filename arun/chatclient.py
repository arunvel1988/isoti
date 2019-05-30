import socket
host = "127.0.0.1"
port = 9000
s = socket.socket()
s.connect((host,port))
#enter data at client
str = raw_input("enter data: ")
while str != "exit":
	s.send(str.encode())
	data = s.recv(1024)
	data = data.decode()
	print("from server: "+data)
	str = raw_input("enter data:")
s.close()


