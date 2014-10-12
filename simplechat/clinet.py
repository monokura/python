import socket

HOST='localhost'
PORT=50007

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print 'wait!'

while 1:
	data = s.recv(1024)
	print '(server) > ', data
	data = raw_input('(client) > ')
	s.send(data)
	if data == "quit":
		break
s.close()
