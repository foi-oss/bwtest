#!/usr/bin/env python

import socket
import sys
import random
import string

args = sys.argv

if len(args) != 3:
	print("Server ip and port argument required! ex.: ./bw_test_server.py localhost 5000")
	
server_address = (args[1], int(args[2]))

# Preparing message
msg = ''
for x in range(0, 1000):
	msg = msg + "0"

# Endless loop for connecting to server
while True:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		print 'Cient: connecting to %s port %s' % server_address
		sock.connect(server_address)
		
		# Sending data (message) to server
		while True:
			sock.sendall(msg)
	    
	except socket.error, v:
		# If socket encountered error - display message and pass to next try in loop
		print "Error: %s" % v[0]
	finally:
		# Clean up the connection
		print 'Client: closing socket'
		sock.close()
