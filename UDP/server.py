from socket import *
serverPort = 331
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:  # the loop makes the socket wait for the client's process packet
    message, clientAddress = serverSocket.recvfrom(2048)
    # coverts bytes to string and capitalizes
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),
                        clientAddress)
