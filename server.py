import socket 
import sys
from _thread import *

HOST = ''
PORT = 8010

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('socket created')

try: 
	s.bind((HOST, PORT))
except socket.error as msg:
	print ('Bind failed')
	sys.exit()

print ('Socket Bind complete')

s.listen(10)
print ('socket now listening')

def clientthread(conn):
	conn.send('nihao'.encode())
	
	while True:
		data = conn.recv(1024)
		reply = 'Server: yo data is ' + data.decode()
		if not data:
			break
			
		conn.sendall(reply.encode())
	conn.close()

while 1:
	conn, addr = s.accept()
	print ('Connected with' + addr[0] + ':' + str(addr[1]))
	
	start_new_thread(clientthread, (conn,))
	
s.close()