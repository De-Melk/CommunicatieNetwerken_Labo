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

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) ##start over ipv4 and UDP
 
sock.bind((socket.gethostname(),50010))     #bind to ip and port
                                            

sock.sendto('0'.encode(), SERVER)

while True:
    data = sock.recv(1024).decode()     #receive message from server

    if data.strip() == 'ready':     # if message is ready start p2p connections
        print('Checked in with server, waiting for Peer')
        break

data = sock.recv(1024).decode()     #recieve other peerw addresses
ipC1, sourceC1, destinationC1, ipC2, sourceC2, destinationC2 = data.split(' ')
sourceC1 = int(sourceC1)
destinationC1 = int(destinationC1)
sourceC2 = int(sourceC2)
destinationC2 = int(destinationC2)

print('\n peer connection established')
print('  ip client1:          {}'.format(ipC1))
print('  source port client1: {}'.format(sourceC1))
print('  dest port client1:   {}\n'.format(destinationC1))
print('  ip client2:          {}'.format(ipC2))
print('  source port client2: {}'.format(sourceC2))
print('  dest port client2:   {}\n'.format(destinationC2))

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) 

sock.bind((socket.gethostname(),50011)) 
sock.sendto('0'.encode(), (ipC1, destinationC1))

print('ready to exchange messages\n')

def listen():       #revieve messages from other peers
    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) 
    sock.bind((socket.gethostname(),50010)) 

    while True:
        data = sock.recv(1024)
        print('\r Peer: {}\n> '.format(data.decode()), end='')

listener = threading.Thread(target=listen, daemon=True)
listener.start()

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM) 
sock.bind((socket.gethostname(),50011)) 

while True:     #send massages to other peers
    msg = input('--> ')
    sock.sendto(msg.encode(), (ipC1, sourceC1))
    sock.sendto(msg.encode(), (ipC2, sourceC2))