#!/usr/bin/python

# Gary Williams
# CS 576
# Prog 1 Due 2/26/17

# This is basic TCP client socket.
# It prompts the user for a string to send to the server to be encoded
# and returned. It specifies special instructions for performing the
# reverse functionality. 

# Directions: Change host to local machine or other. Run and answer
#   the prompt to send the message to be encoded by the server and
#   returned by default. Specify 'D' to decode the message and perform
#   the opposite functionality.
 
import socket

HOST = 'nibbler'
PORT = 5760
msg = raw_input("Enter msg < 256 characters('D' first letter to decode): ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(msg)
data = s.recv(256)
s.close()
print 'Received ', repr(data)
