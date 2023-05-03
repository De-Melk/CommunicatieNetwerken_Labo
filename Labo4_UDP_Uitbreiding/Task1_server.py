import socket
import threading
import os

clientList = []     #list with all connected clients

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )  #start over ipv4 and UDP
s.bind((socket.gethostname(),4444))     #server ip and portnumber
print("\t\t\t====>  UDP P2P APP  <=====")
print("=============================================="*2)

#ip,port = input("Enter IP address and Port number: ").split()
ip = socket.gethostname()       #Server ipaddres
port = 2222                     #port used by other chatter


def main():          #receive message from client
    while True:
        msg, addr = s.recvfrom(1024)
        #print(msg.decode())
        #print(addr)
        #print(((msg.decode().split(":"))[1]).strip())
        print(clientList)

        if clientList.count(addr) == 0:     #add clients not in list
            clientList.append(addr)
        
        if ((msg.decode().split(":"))[1]).strip() == "quit":        #remove client from list when message == quit
            clientList.remove(addr)
            print(clientList)

        for i in clientList:        #send message to all clients in list
             s.sendto(msg , i)
                


        
main()
