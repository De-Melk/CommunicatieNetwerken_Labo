import socket
import threading
import os

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
print("\t\t\t====>  UDP CHAT APP  <=====")
print("=============================================="*2)
nm = input("ENTER YOUR NAME : ")
print("\nType 'quit' to exit.")

#ip,port = input("Enter IP address and Port number: ").split()
ip = socket.gethostname()       #Client ipaddres
port = 2222                     #port used by other chatter/server
print("client connected on: ", ip, port)

def send():
    while True:
        ms = input(">> ")
        if ms == "quit":
            os._exit(1)
        sm = "{}  : {}".format(nm,ms)
        s.sendto(sm.encode() , (ip,int(port)))

x1 = threading.Thread( target = send )

x1.start()