import threading
import socket

HOST = "192.168.7.67"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
DISCONNECT_MESSAGE = "!DISCONNECT"  #message to send to exit and disconnect 
connected = True


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #start TCP over ipv4 and TCP
s.connect((HOST, PORT))                #connect to Server via IP and port
print("[Connected to server]")

def recv_msg():                #to recveive messages
    global connected
    while connected:
        recv_msg = s.recv(1024)         #receive, decode and print in terminal
        print("[Server] ->",recv_msg.decode('UTF-8'))

def send_msg():             #to send messages
    global connected
    while connected:
        send_msg = input(str())         #send input string
        s.send(send_msg.encode('UTF-8'))        
        if send_msg == DISCONNECT_MESSAGE:      #stop program if disconnect message
            connected = False

t = threading.Thread(target=recv_msg)       #initiate, start recv_msg in other thread
t.start()

send_msg()
