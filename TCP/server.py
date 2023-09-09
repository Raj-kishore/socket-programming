from socket import *
serverPort = 331
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    # new socket (e.g. connectionSocket) is created and dedicated the particular client
    # after connection is established with client
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
# tcp ensures reliable data trasfer and in order unlike UDP
# Although UDP ensures maximum throughput due to no handshakings involved before sending any data
# serverSocket is still open to welcome another client
