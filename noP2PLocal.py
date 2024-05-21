from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class NodeP2P:
    def __init__(self,port):
        self.port = port
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('127.0.0.1',port))
        self.serverSocket.listen()

def handleClient(socketClient, ClientAdress):
    while True:
        req = socketClient.recv(1024)

        print(f"{ClientAdress}: {req.decode()}")

        rep = "gatos.png, segredosdocin.zip"

        socketClient.send(rep.encode())

porta = int(input())
No = NodeP2P(porta)
porta_vizinho = int(input())
No.clientSocket.connect(('127.0.0.1',porta_vizinho))

print("Servidor esperando requisições")
socketVizinho, enderecoVizinho = No.serverSocket.accept()
print(f"Cliente {enderecoVizinho} estabeleceu a comunicação")
Thread(target=handleClient,args=[socketVizinho, enderecoVizinho]).start() 

while True:

    data = input()

    No.clientSocket.send(data.encode())

    rep = No.clientSocket.recv(1024)

    print(f"Resposta do servidor:{rep}")