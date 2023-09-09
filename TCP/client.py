from socket import *
serverName = 'localhost'
serverPort = 331
# SOCL_STREAM indicates that the process uses a tcp socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Handshaking for TCP connection establishment from both ends before sending any message.
# Make sure the server is running before running client.py unlike udp, else it will throw ConnectionRefuseError
# 1. the TCP server must be running as a process before the client attempts to initiate contact
# 2. the server program must have a special socket that welcomes some initial contact from a client process running on an arbitrary host.
# The three-way handshake, which takes place within the transport layer, is completely invisible to the client and server programs.
clientSocket.connect((serverName, serverPort))
message = input('Input lowercase sentence:')
clientSocket.send(message.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
