from socket import *
serverName = 'localhost'
serverPort = 331
# AF_INET indicates the network is using ipv4
# SOCK_DGRAM which tells its UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)  # creates client socket.
message = input('Input lowercase sentence:')
# encode method converts string to byte stream that is sent to process's socket
clientSocket.sendto(message.encode(), (serverName, serverPort))
# after sending the packet, client waits to recieve data from the server
# 2048 is the given buffer size
# serverAddress keeps server address and port information. But UDP doesn't care.
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(serverAddress)
print(modifiedMessage.decode())
clientSocket.close()
