#!/usr/bin/python3
# file: server.py
# content: server testing app
# created: 20210118
# author: Roch Schanen

import socket
ip, pt = "0.0.0.0", nnnnn


# create socket
sh = socket.socket()

print(f'Bind socket to {ip}:{pt}', end = '')
sh.bind((ip, pt))
print(f' ok')

n = 2

while(n):

	print(f'Start listening...', end = '')
	sh.listen()

	clientSocket, clientAddress = sh.accept()
	print(f' {clientAddress} connected')

	print(f'Receiving message...', end = '')
	ms = clientSocket.recv(64).decode() # get 64 bytes
	print(f'"{ms}" received')

	clientSocket.close()

	n -= 1

sh.close()
