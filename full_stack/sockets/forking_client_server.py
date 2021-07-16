#!/usr/bin/env python 

import os 
import socket 
import threading 
import socketserver 
 
 
SERVER_HOST = 'localhost' 
SERVER_PORT = 0 # tells the kernel to pickup a port dynamically 
BUF_SIZE = 1024 
ECHO_MSG = 'Hello echo server!' 
 
 
class ForkedClient(): 
    """ A client to test forking server"""     
    def __init__(self, ip, port): 
        # Create a socket 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server 
        self.sock.connect((ip, port)) 
     
    def run(self): 
        """ Client playing with the server""" 
        # Send the data to server 
        current_process_id = os.getpid() 
        print ('PID %s Sending echo message to the server : "%s"' % (current_process_id, ECHO_MSG)) 
 
        sent_data_length = self.sock.send(bytes(ECHO_MSG, 'utf-8')) 
 
        print ("Sent: %d characters, so far..." %sent_data_length) 
         
        # Display server response 
        response = self.sock.recv(BUF_SIZE) 
        print ("PID %s received: %s" % (current_process_id, response[5:])) 
     
    def shutdown(self): 
        """ Cleanup the client socket """ 
        self.sock.close() 
       