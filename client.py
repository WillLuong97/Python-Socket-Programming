import socket
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

#The server will run on a local host IP Address, which means any devices that connects to the same wifi as 
#the server device can access it
#****** To run a server over the internet, find your device public IP address and any devices that connects to the internet would be able to 
#connect to the server
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
#connecting to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#Sending a message to the server: 
def send(msg):
    #Encode the message to the server format before sending it out
    message = msg.encode(FORMAT)
    #The first message sent out has the lenght of the entire message
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    #make sure that the entire message got sent out has the length of 64 bytes
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello Everyone!")
send("Hello World!")
input()
send("Hello Saundra!")


send(DISCONNECTED_MESSAGE)

