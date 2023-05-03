
import socket
import threading

#msgFromClient       = "Hello UDP Server"
#bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.7.67", 20001)
bufferSize          = 1024

def receive_messages(UDPClientSocket):
    # loop to continuously receive and display messages from the server
    while True:
        #msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        #msg = "Message from Server {}".format(msgFromServer[0])
       # print(msg)
       break

def send_messages(UDPClientSocket):
    # loop to continuously read user input and send messages to the server
    print("Type a message to send (or 'exit' to quit): ")
    while True:
        message = input()
        bytesToSend = str.encode(message)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

def main():
    try:
        # connect to the server
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # start separate threads to handle receiving and sending messages
        receive_thread = threading.Thread(target=receive_messages, args=(UDPClientSocket,))
        receive_thread.start()

        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        
        send_thread = threading.Thread(target=send_messages, args=(UDPClientSocket,))
        send_thread.start()

        # wait for both threads to complete before closing the connection
        receive_thread.join()
        send_thread.join()
    except ConnectionRefusedError:
        print("Could not connect to server.")
    except:
        print("An error occurred while running the client.")
        raise

if __name__ == "__main__": 
    main()
