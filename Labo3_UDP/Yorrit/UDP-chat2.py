import socket
import threading
import os

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
s.bind((socket.gethostname(),3333))     #server ip and portnumber
print("\t\t\t====>  UDP CHAT APP  <=====")
print("=============================================="*2)
nm = input("ENTER YOUR NAME : ")
print("\nType 'quit' to exit.")

#ip,port = input("Enter IP address and Port number: ").split()
ip = socket.gethostname()       #Client ipaddres
port = 2222                     #port used by other chatter
print("client connected on: ", ip, port)

def send():             #send message to server
    while True:
        ms = input(">> ")
        if ms == "quit":
            os._exit(1)
        sm = "{}  : {}".format(nm,ms)
        s.sendto(sm.encode() , (ip,int(port)))

def rec():          #receive message from client
    while True:
        msg = s.recvfrom(1024)
        print("\n<< " +  msg[0].decode()  )
        print(">> ")

        
x1 = threading.Thread( target = send )
x2 = threading.Thread( target = rec )

x1.start()
x2.start()