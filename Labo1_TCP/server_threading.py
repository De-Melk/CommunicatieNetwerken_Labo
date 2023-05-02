import threading
import socket

HOST = "192.168.7.67"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DISCONNECT_MESSAGE = "!DISCONNECT"  #message to send to exit and disconnect 
ADDR = (HOST, PORT)
connected = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #start TCP over ipv4 and TCP
s.bind(ADDR) #bind program to ip and port

def recv_msg(conn, addr):   #to recveive messages from client
    global connected
    while connected:
        recv_msg = conn.recv(1024)          #receive, decode and print in terminal
        print(f"[{addr}] ->", recv_msg.decode('UTF-8'))
        if recv_msg.decode('UTF-8') == DISCONNECT_MESSAGE:      #exit and disconnect
            conn.sendall("[Disconnected]".encode('UTF-8'))
            conn.close()
            connected = False
            print(f"[{addr}] ->", "CLOSED THE CONNECTION!")

def send_msg(conn, addr):       #to send messages
    global connected
    while connected:
        try:
            send_msg = input(str())         #send input string
            conn.sendall(send_msg.encode('UTF-8'))
        except:
            print("[No Client] can't send message when no client is connected") #no client can't send

def start():
    global connected
    while not connected:
        conn, addr = s.accept()     #accept incomming clients
        print(f"[Connected] client {addr} connected")
        connected = True
        t_recv = threading.Thread(target=recv_msg, args=(conn, addr))       #start send and receive threads
        t_recv.start()
        t_send = threading.Thread(target=send_msg, args=(conn, addr))
        t_send.start()

print("[STARTING] server is starting...")
s.listen()
print(f"[LISTENING] Server is listening on {HOST}")

while True:
    start()
