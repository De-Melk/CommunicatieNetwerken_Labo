import os.path
import socket

HOST = "192.168.7.67"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DISCONNECT_MESSAGE = "!DISCONECT"   #message to send to exit and disconnect
FILESHARE_MESSAGE = "!FILE"         #message to send to send a file
ADDR = (HOST, PORT)
SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #start TCP over ipv4 and TCP
s.bind(ADDR)    #bind program to ip and port


def handle_client(conn, addr):
    print(f"[Connected] client {addr} connected")

    connected = True
    while connected:
        data = conn.recv(1024)
        if data.decode('UTF-8') == DISCONNECT_MESSAGE:  #diconnect is disconnect message is send 
            connected = False
            response = "[Disconected]".encode('UTF-8')

        elif data.decode('UTF-8') == FILESHARE_MESSAGE:     #fileshare
            #Receiving the filename from the client.
            filename = conn.recv(SIZE).decode('UTF-8')
                
            print(f"[RECV] Receiving the filename.")
            file = open("Labo2_TCP_Uitbreiding/data_recv/" + filename, "w") #create file
            conn.send("Filename received.".encode('UTF-8'))     #send confirmation

            #Receiving the file data from the client.
            data = conn.recv(SIZE).decode('UTF-8')
            print(f"[RECV] Receiving the file data.")
            file.write(data) #write data to file
            conn.send("File data received".encode('UTF-8'))     #send confirmation

            connected = False
            response = "[Disconected]".encode('UTF-8')      #disconect

        else:
            print(f"[{addr}] ->", data.decode('UTF-8'))     #print received message
            response = "[MessageReceived]".encode('UTF-8')

        conn.sendall(response)
    
    print(f"[Disconected] client {addr} disconected")
    conn.close() #close connection to client


def start():
    s.listen()      #listen for incomming client connections
    print(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn, addr = s.accept()     #accept connections
        handle_client(conn, addr)
        
print("[STARTING] server is starting...")
start()