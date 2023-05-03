import socket

HOST = "192.168.7.67"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
DISCONNECT_MESSAGE = "!DISCONECT"       #message to send to exit and disconnect 
FILE_SHARE_MESSAGE = '!FILE'            #message to send to send a file
FORMAT = 'UTF-8'
SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        #start TCP over ipv4 and TCP
    s.connect((HOST, PORT))          #connect to Server via IP and port

    connected = True
    while connected:
        tekst = input('geef input: ').encode(FORMAT)   #encode en decode voor binair formaat
        s.sendall(tekst)            #send input message to server
        
        if tekst.decode(FORMAT) == FILE_SHARE_MESSAGE:      #send file
            # opening and reading file
            print("Plaats de file in './data_send'!")
            fileName = input("Geef de filenaam: ")
            file = open('Labo2_TCP_Uitbreiding/data_send/' + fileName, 'r')
            data = file.read()

            # Sending the filename to the server.
            s.send(fileName.encode(FORMAT))
            msg = s.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")           #confirm from server

            # Sending the file data to the server.
            s.send(data.encode(FORMAT))
            msg = s.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")           #confirm from server

            # Closing the file..
            file.close()

            # Closing the connection from the server.
            connected = False

        data = s.recv(1024)         #receiving and printing data from server
        print(data.decode(FORMAT))

        if tekst.decode(FORMAT) == DISCONNECT_MESSAGE:      #stop program if disconnect message
            connected = False