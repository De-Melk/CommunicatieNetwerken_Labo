import threading
import socket

HOST = "192.168.173.135"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
DISCONNECT_MESSAGE = "!DISCONNECT"
connected = True

def receive_messages(sock):
    # loop to continuously receive and display messages from the server
    while True:
        message = sock.recv(1024)
        if not message:
            # end of stream, server has disconnected
            break
        
        print(f" Received: {message.decode().strip()} ")
        #print("Type a message to send (or 'exit' to quit): ")

def send_messages(sock):
    # loop to continuously read user input and send messages to the server
    print("Type a message to send (or 'exit' to quit): ")
    while True:
        message = input()
        if message == "exit":
            # close the connection and end the loop
            sock.close()
            break
        sock.sendall(message.encode())

def main():
    try:
        # connect to the server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

        # start separate threads to handle receiving and sending messages
        receive_thread = threading.Thread(target=receive_messages, args=(sock,))
        receive_thread.start()

        send_thread = threading.Thread(target=send_messages, args=(sock,))
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

