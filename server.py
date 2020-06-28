#Pyhon server:
import socket
#we will put different message handling in seperate threads for each clients that connects to our server
#this way, each client does not have to wait until their request can be handled. 
import threading

#The first message to the server from the client is always going to be a header
# and this header can only contain 64 bytes of memory worth of characters
HEADER = 64
#Define a port for the server to run on:
PORT = 5050
#Header encoding format: 
FORMAT = "utf-8"
#Message that will be sent to the server to notify a client has been disconnected
#Once the server recieves this message, the server will close out the connection with the particular clients
DISCONNECTED_MESSAGE = "!DISCONNECT FROM SERVER"

#the server will run on the local device that the code is running on
#get the ipaddress of the hosting device by name 
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
#socket to allow this device to connect to other connection: 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #what kind of devices that our server would accept connection from, and stream data from the same socket
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    connected = True
    while connected:
        #Checking the length of the header and decode its encoded format into a string
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: #make sure that there is a contents in the message being sent to the server from the clients 
            msg_length = int(msg_length)
            #letting the server know how many bytes we will recive from client message 
            msg = conn.recv(msg_length).decode(FORMAT)
            #handle the client disconnection
            if msg == DISCONNECTED_MESSAGE:
                connected = False

            #Seeing the message and its contents  
            print(f"[{addr}] {msg}")
            #the server will send a message to the client
            conn.send("Message recieved".encode(FORMAT))

    conn.close()
        
#waiting and listening for connection and sending the request to the handle_client()
def start():
    #The server begins listening
    server.listen()
    #Notifying which IP address the server is running on
    print(f"[LISTENING] Server is listening on {SERVER}")
    #The server will listen infinitely until we want to stop
    while True:
         #the event listener will recieve the address of the connection origin and its port
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #Display the amount of active connection:
        #the amount of threads represent the amount of clients connected 
        #However, since we always have a thread running in the background, we have to minus it out of our connection list because that thread is 
        #listening for new connection and an actual connection
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
print("[STARTING] server is starting...")
start()

