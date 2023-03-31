import socket
import threading
import os

clientList = []

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
s.bind((socket.gethostname(),4444))     #server ip and portnumber
print("\t\t\t====>  UDP P2P APP  <=====")
print("=============================================="*2)

#ip,port = input("Enter IP address and Port number: ").split()
ip = socket.gethostname()       #Client ipaddres
port = 2222                     #port used by other chatter


def rec():          #receive message from client
    while True:
        msg, addr = s.recvfrom(1024)
        #print("\n<< " +  msg[0].decode()  )
        #print(">> ")
        print(addr)
        for i in clientList:
            if i != addr:
                clientList.append(addr)

        for i in clientList:
             #s.sendto(msg , (i,int(clientList[i])))
             s.sendto(msg , i)
                


        
rec()
