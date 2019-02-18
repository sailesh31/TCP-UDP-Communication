from socket import *                  #allows us to create sockets in python by importing socket module.
import random

def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr


serversidePort = 12121              #Set the port number of the server.

serversideSocket = socket(AF_INET,SOCK_STREAM)
#creates a socket on the server side.
#AF_INET describes the underlying network type.
#SOCK_STREAM indicates that the socket is of TCP type.

serversideSocket.bind(('' ,serversidePort))
#Here serversideSocket will be our welcome socket.The port number is binded to the socket.

serversideSocket.listen(1)
#server listens for TCP connection.The parameter in the bracket specifies the no. of connections to be queued.

print 'Waiting for client \n'

while 1:
   connectionSocket, addr = serversideSocket.accept()
   #A new socket is created when a connection from client is received after handshake through serverportsocket.
   #data transfer is facilitated between client and the server through this socket.    
   print 'Accessed from client of IP =',addr[0]
   raw_data = connectionSocket.recv(1024)
   intermediate_data= raw_data[1::].split()
   intermediate_data1=[int(x) for x in intermediate_data]
   intermediate_data1=insertionsort(intermediate_data1) #sorting the data.
   result=''
   i=0
   while(i<len(intermediate_data1)):
       result=result+' '+str(intermediate_data1[i])
       i+=1
   connectionSocket.send(result) #sending the sorted data back to the client.
   print '\tResponded to IP =',addr[0],'by sending the sorted list\n'
   connectionSocket.close()    #We close only the connectionSocket.Serversocket still remains open.
