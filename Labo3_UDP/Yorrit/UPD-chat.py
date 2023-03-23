import socket
import threading
import os

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
<<<<<<< Updated upstream:Labo3_UDP/Yorrit/UPD-chat.py
s.bind((socket.gethostname(),2222))
=======
s.bind(("192.168.7.67",2222))
>>>>>>> Stashed changes:Labo3_UDP/Yorrit/test.py
print("\t\t\t====>  UDP CHAT APP  <=====")
print("=============================================="*2)
nm = input("ENTER YOUR NAME : ")
print("\nType 'quit' to exit.")

#ip,port = input("Enter IP address and Port number: ").split()
ip = socket.gethostname()
port = 3333
print("client connected on: ", ip, port)

def send():
    while True:
        ms = input(">> ")
        if ms == "quit":
            os._exit(1)
        sm = "{}  : {}".format(nm,ms)
        s.sendto(sm.encode() , (ip,int(port)))

def rec():
    while True:
        msg = s.recvfrom(1024)
        print("\n<< " +  msg[0].decode()  )
        print(">> ")
x1 = threading.Thread( target = send )
x2 = threading.Thread( target = rec )

x1.start()
x2.start()