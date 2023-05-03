# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:10:59 2023

@author: Prabhu Vijayan
"""

import socket

clientport1 = 50002
clientport2 = 50003
print("running")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #start over ipv4 and UDP

sock.bind((socket.gethostname(),50001)) #Bind program to ip and port

while True:
    clientcount = [] #list with all connected clients

    while True:
        data, address = sock.recvfrom(128)      #receive data and other peer adress from server

        print('Connection from: {}'.format(address))
        clientcount.append(address) #add client to list      

        sock.sendto('ready'.encode(), address) #send ready to client

        if len(clientcount) == 3:       #if list has 3 clients start peer to peer connections
            print('minimum Clients count reached: Exchanging Information')
            break

    c1 = clientcount.pop()      #get all peer addressen from list 
    c1_addr, c1_port = c1
    c2 = clientcount.pop()
    c2_addr, c2_port = c2
    c3 = clientcount.pop()
    c3_addr, c3_port = c3

    #send peer addressen to other peers
    sock.sendto('{} {} {} {} {} {}'.format(c2_addr, c2_port, clientport2, c1_addr, c1_port, clientport1).encode(), c3)  
    sock.sendto('{} {} {} {} {} {}'.format(c1_addr, c1_port, clientport1, c3_addr, c3_port, clientport2).encode(), c2)
    sock.sendto('{} {} {} {} {} {}'.format(c2_addr, c2_port, clientport2, c3_addr, c3_port, clientport2).encode(), c1)