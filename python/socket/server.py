import time, socket, sys
print('Server')
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 1234
soc.bind((ip, port))
soc.listen(1)
print('Waiting for connection...')
con, add = soc.accept()
print("Received connection")
print('bye to quit')
while True:
   message = raw_input('server > ')
   if message == 'bye':
      message = 'bye'
      con.send(message.encode())
      print("\n")
      break
   con.send(message.encode())
   message = con.recv(1024)
   print('client>'+ message)
