#!/usr/bin/python

# Gary Williams
# CS 576
# Prog 2 Due 4/3/17

# This is a basic UDP client socketed connection.
# It prompts the user for the message to be sent,
# echos that message before sending it to the
# and printing the reply. Msg sent to server over
# port 5432 and reply is heard on 5433.
#
# referenced: https://pymotw.com/2/socket/udp.html

import socket
import sys

msg = raw_input("Enter short message: ")
while not msg:
   msg = raw_input("Enter a valid message: ")

#Create socket before trying to send
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5432)

try:

   print >>sys.stderr, 'Sending: "%s"' % msg
   sent = sock.sendto(msg, server_address)

   #Msg sent, program will block until recv
   data, server = sock.recvfrom(5433)
   print >>sys.stderr, 'Received: "%s"' % data

finally:
   sock.close()
