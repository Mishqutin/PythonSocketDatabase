

import socket               # Import socket module
import os

an = sl4a.Android()

os.chdir("sdcard/sz/desk/mhosted")

s = socket.socket()         # Create a socket object
host = "0.0.0.0"            # Change it to your IP you want to use.
port = 12345               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   try:
      c, addr = s.accept()           # Accept connection. c is class socket. Use it to send and recv data from client.
      if type(c)==socket.socket:
         cip, cport = addr          # Unpack tuple. cip = client ip.
         
         print('Got connection from')
         print(cip)
         
         c.send(b"\nHello")     # Send data to client.
         
         print("Awaiting reply...")
         
         reply = str(c.recv(1024))[2:-1]   # Receive 1024 bytes of data or less. Convert to string and remove b' and '
         print(reply)
         
         if reply=="&list":
            data = str(os.listdir())           # List directory content to var data if client replied "&list"
         elif reply[0:6]=="&write":   # Client can reply &write <file_name> <any content ..... to create new file on server
            a = reply.split()
            f = open(a[1], 'w')
            f.write(' '.join(a[2:]))
            f.close()
            data = "File written."
         else:                      # Client can specify file name only and the content will be returned
            f = open(reply, 'r')
            data = f.read()
            f.close()
         c.send(data.encode())   # Convert data var with string to bytes and send it to client
         c.close()         # Close connection. Socket c won't receive data anymore.
   except:
      try: c.close()
      except: pass