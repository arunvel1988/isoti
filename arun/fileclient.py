import socket 
host = "localhost"
port=6767
s= socket.socket()
s.connect((host,port))
filename = raw_input("enter filename ")
s.send(filename.encode())
content = s.recv(1024)
print(content.decode())
s.close()
