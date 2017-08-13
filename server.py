#!/usr/bin/python

# Gary Williams
# CS 576
# Prog 1 Due 2/26/17

# This is a basic server TCP socket connection.
# It connects to the localhost and specified port
# and listens for packets with a max 256 characters.
# The string is encoded by changing each character
# to the next character in the ASCII table by default.
# If the string is prefaced by a 'D', then the string
# is decoded by doing the opposite.

# Directions: Change host to local machine or other.
#   Run and wait for output for successful connection
#   or error.

import socket
import sys

HOST = 'nibbler'	#localhost used for dev
PORT = 5760
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enclosed bind in try block to catch busy port
try:
   s.bind((HOST, PORT))
except Exception as inst:
   print inst
   print 'Host: ' + HOST + '  Port: ' + str(PORT)
   sys.exit(0)

s.listen(1)
conn, addr = s.accept()
print 'Connected by ', addr
tmpRay = []
fixed = []
while 1:
   data = conn.recv(256)
   if not data: break
   print 'Received: ', data
   ray = list(data)
   for i in ray:
      tmpRay.append(ord(i))
   if tmpRay[0] == 68:		# Test for 'D'
      new_list = [x-1 for x in tmpRay]
      new_list = new_list[1:]
   else:
      new_list = [x+1 for x in tmpRay]
   for i in new_list:
      fixed.append(chr(i))
   conn.sendall(''.join(fixed))
conn.close()
