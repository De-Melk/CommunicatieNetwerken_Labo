# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:10:03 2023

@author: Prabhu Vijayan
"""

import socket
import threading

SERVER = (socket.gethostname(),50001)   #"To fill up"
                                        #Server IP and Port               

print('connecting to the SERVER')

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) #"To fill up"
 
sock.bind((socket.gethostname(),50010))     #"To fill up"
                                            

sock.sendto('0'.encode(), SERVER)

while True:
    data = sock.recv(1024).decode()

    if data.strip() == 'ready':
        print('Checked in with server, waiting for Peer')
        break

data = sock.recv(1024).decode()
ip, source, destination = data.split(' ')
source = int(source)
destination = int(destination)

print('\n peer connection established')
print('  ip:          {}'.format(ip))
print('  source port: {}'.format(source))
print('  dest port:   {}\n'.format(destination))

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) #"To fill up"

sock.bind((socket.gethostname(),50011)) #"To fill up"
sock.sendto('0'.encode(), (ip, destination))

print('ready to exchange messages\n')

def listen():
    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) #"To fill up"
    sock.bind((socket.gethostname(),50010)) #"To fill up"

    while True:
        data = sock.recv(1024)
        print('\r Peer: {}\n> '.format(data.decode()), end='')

listener = threading.Thread(target=listen, daemon=True)
listener.start()

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) #"To fill up"
sock.bind((socket.gethostname(),50011)) #"To fill up"

while True:
    msg = input('--> ')
    sock.sendto(msg.encode(), (ip, source))