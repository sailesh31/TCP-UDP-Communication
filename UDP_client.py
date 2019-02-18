from socket import *       #allows us to create sockets in python by importing socket module.
import random

serverName='172.16.81.51'  #IP address of the server to route the data.

serverPort=12121           #Set the port number of the server.

clientsideSocket=socket(AF_INET,SOCK_DGRAM)
#creates a socket on the client side.
#AF_INET describes the underlying network type.
#SOCK_DGRAM indicates that the socket is of UDP type.

raw_data=raw_input("Enter the numbers to be sorted with a space:")   #input
i=0
print raw_data
raw_data = " " + raw_data

clientsideSocket.sendto(raw_data,(serverName,serverPort))
#We attach the destination address to the data and send it to the client socket from where it is sent to server.


print 'Request sent to server',serverName
sorted_data,serverAddress=clientsideSocket.recvfrom(2000)
#Receive data from internet at clients socket.socket.recvfrom(k) k is the buffer size.

print 'Response received from server'
print sorted_data[1::]

print 'connection closed'
clientsideSocket.close()
#Socket is closed.
