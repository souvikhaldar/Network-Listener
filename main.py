import socket
# the port on which I'm listening for incoming data
listener_port = 7005

# create a socket which can deal with IPv4 (AF_INET) address
# and STREAM of data
listener_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind this socket to the hostname of the machine on 
# which it is running and a specified port
listener_socket.bind((socket.gethostname(),listener_port))

# now we'll be accepting and queing up a maximum of 
# 5 connections at a time and refusing the rest, if any
listener_socket.listen(5) 

while True:
    # accept incoming request
    (client_socket,address) = listener_socket.accept()
    print("Connected by: ",address)

    # now read all data sent by client and echo it
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Incoming data: ",data)
        client_socket.sendall(data)
        
         