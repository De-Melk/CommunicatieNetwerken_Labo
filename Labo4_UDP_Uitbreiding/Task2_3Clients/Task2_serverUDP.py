# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:10:59 2023

@author: Prabhu Vijayan
"""

import socket

clientport1 = 50002
clientport2 = 50003
print("running")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #"To fill up"

sock.bind((socket.gethostname(),50001)) #"To fill up"

while True:
    clientcount = [] #"To fill up"

    while True:
        data, address = sock.recvfrom(128)

        print('Connection from: {}'.format(address))
        clientcount.append(address) #"To fill up"

        sock.sendto('ready'.encode(), address) #"To fill up"

        if len(clientcount) == 3:
            print('minimum Clients count reached: Exchanging Information')
            break

    c1 = clientcount.pop()
    c1_addr, c1_port = c1
    c2 = clientcount.pop()
    c2_addr, c2_port = c2
    c3 = clientcount.pop()
    c3_addr, c3_port = c3

    sock.sendto('{} {} {} {} {} {}'.format(c2_addr, c2_port, clientport2, c1_addr, c1_port, clientport1).encode(), c3)
    sock.sendto('{} {} {} {} {} {}'.format(c1_addr, c1_port, clientport1, c3_addr, c3_port, clientport2).encode(), c2)
    sock.sendto('{} {} {} {} {} {}'.format(c2_addr, c2_port, clientport2, c3_addr, c3_port, clientport2).encode(), c1)