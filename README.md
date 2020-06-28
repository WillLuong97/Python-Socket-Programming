### Python Web Socket Programming

This program will create a python web server that can recieve any messages from the clients and reply with a message to the client

The message from the client to the server would have a memory constraints of 64-bytes. This way, the server would not risk receiving message that are too large in memory space 

## The SERVER

The server is able to constantly running and listening for any requests comming from its clients through its implementation of socket and threading. 

The server will run on a local host IP Address, which means any devices that connects to the same wifi as the server device can access it
To run a server over the internet, find your device public IP address and any devices that connects to the internet would be able to connect to the server.

```
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
#connecting to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
```

We must import Socket for the server to work in the first place.

```
    import socket

```

To apply a constraint on the client message being sent into the server. The client must include a header with it. In this case, the header would be the the first messsage from the client. The header will determine the length of the message and this is where we intializes the 64 byte constraint

```
    HEADER = 64
```

In addition, the header/message must also be encoded with a standard server side encoding format. In our server, the header format would be "utf-8".

```
FORMAT = "utf-8"
```

The client is able to connect and disconnect at any instances. However, the server must have a standard protocol to cleanly close out any current connection instances from the particular clients that are looking to disconnect. In our system, the server will have a disconnected message that it is looking for when the client is seeking to connect.

```
DISCONNECTED_MESSAGE = "!DISCONNECT FROM SERVER"

#From server end: 
if msg == DISCONNECTED_MESSAGE:
    connected = False


#From client end: 
send(DISCONNECTED_MESSAGE)
```

To use threading, we must import it from python library

```
import threading
```
Each thread represents a connection that has just been made to the server from the clients. 

```
conn, addr = server.accept()
thread = threading.Thread(target=handle_client, args=(conn, addr))
thread.start()
```

However, since we always have a thread running in the background, we have to minus it out of our connection list because that thread is listening for new connection and an actual connection
```
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
```


## The CLIENT

The client will connect to the server using the IP address of the server. In this current commit, the server IP address is local to the device that is running the server. As a result, the client must connect to the same wifi that the server is running to be able to access the server. 

To make a connection to the server, we would use the following codes:  

```
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    #connecting to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
```

To send a message to the server, we would create a method send() with the message to be sent out as the paremeter and call it as below:

```
send("Hello World!")
input()
send("Hello Everyone!")
send("Hello World!")
input()
send("Hello Saundra!")


send(DISCONNECTED_MESSAGE)

```
