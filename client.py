#!/usr/bin/python3
# file: client.py
# content: client testing app
# created: 20210118
# author: Roch Schanen

import socket
# ip, pt = "192.168.1.xxx", nnnnnn
ip, pt = "xxx.xxx.xxx.xxx", nnnnnn

# create socket
sh = socket.socket()

print(f'Connecting to {ip}:{pt}', end = '')
sh.connect((ip, pt))
print(f' ok')

ms = f"hello"

print(f'Send "{ms}"', end = '')
sh.sendall(ms.encode())
print(f' ok')

print(f'Close connection', end = '')
sh.close()
print(f' ok')
