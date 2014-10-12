import socket

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
soc, addr = s.accept();
print 'Connected by', addr
print 'Go ahead!'

while 1:
	data = raw_input('(server) > ')
	soc.send(data)
	data = soc.recv(1024)
	print '(client) > ',data
	if data == 'quit':
		break
soc.close()
