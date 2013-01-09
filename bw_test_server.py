#!/usr/bin/env python

import socket
import sys

args = sys.argv

if len(args) != 2:
	print("Port argument required! ex.: ./bw_test_server.py 5000")

port = args[1]
server_address = ('0.0.0.0', int(port))

# Setting up server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Server: starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    print 'Server: waiting for a connection'
    
    # Accepting client connection
    connection, client_address = sock.accept()

    datan = 0

    try:
        print 'Server: connection from ', client_address

        # Receiving data
        while True:
            data = connection.recv(1000)
			# If no data received terminate loop
            if not data:
				break
            
    finally:
        # Clean up the connection
        connection.close()
