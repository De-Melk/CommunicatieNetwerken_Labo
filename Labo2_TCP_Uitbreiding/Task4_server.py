import threading
import socket

HOST = "192.168.7.67"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (HOST, PORT)
connected = False

# create socket object for the server
#AF_INET = IPV4  SOCK_STREAM = TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket object to an address and port
server_socket.bind(ADDR)

# listen for incoming connections
server_socket.listen()
print("Server is listening for incoming connections...")

# list to keep track of all client sockets
sockets = []

# function to handle incoming connections
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address} has been established!")
    
    # add client socket to list
    sockets.append(client_socket)

    while True:
        # receive message from client
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")

        # send message to all connected clients except sender
        for sock in sockets:
            if sock != server_socket and sock != client_socket:
                sock.sendall(message.encode())

# main loop to accept incoming connections
while True:
    # accept incoming connections
    client_socket, client_address = server_socket.accept()

    # create a new thread to handle the connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

