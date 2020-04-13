import time, socket, sys
print('Client')
soc = socket.socket()
port = 1234
soc.connect(("127.0.0.1", port))
print("Connected...\n")
print('Enter [bye] to exit.')
while True:
   message = soc.recv(1024)
   if message == 'bye':
	break
   print("server>"+ message)
   message = raw_input(str("client> "))
   if message == "bye":
      message = "bye"
      soc.send(message.encode())
      print("\n")
      break
   soc.send(message)
