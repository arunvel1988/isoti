import socket
host="localhost"
port = 6767
s = socket.socket()
s.bind((host,port))
s.listen(1)
#wait till client accepts connection
c, addr =  s.accept()
print("client accepted connection:")
fname = c.recv(1024)
#accept file name from client
fname = str(fname.decode())
print("file name received from client" +fname)
try:
	f = open(fname, 'rb')
	content = f.read()
	c.send(content)
	print("file content send:")
	f.close()
except FileNotFoundError:
	c.send(b'file does not exist')
c.close()
	
