#!/usr/bin/python

# Gary Williams
# CS 576
# Prog 2 Due 4/3/17

# This is a basic UDP socketed server. It connects to the
# local host and listens to port '5432' as specified in
# the assignment. If a message is received, it
# concatenates a reply message and then send that reply
# over port '5433'. Because UDP is a connection-less
# protocol, the server merely listens and replies.

import socket
import sys

gibberish = "- Roger Roger. Read you loud and clear"

#Create socket and save port in address before binding
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5432)
print >>sys.stderr, 'Starting up on %s port %s' % server_address
sock.bind(server_address)

#Receive loop; when data received, concat and reply
while 1:
   print >>sys.stderr, 'Waiting to receive message'
   data, address = sock.recvfrom(5433)

   print >>sys.stderr, 'Received %s bytes from %s' % (len(data), address)
   print >>sys.stderr, data

   if data:
      data = data + gibberish
      sent = sock.sendto(data, address)
      print >>sys.stderr, 'Sent %s bytes back to %s' % (sent, address)
