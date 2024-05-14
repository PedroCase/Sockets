from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

serverSocket = socket(AF_INET, SOCK_STREAM)


serverSocket.bind(('127.0.0.1',12345))
serverSocket.listen()

def handleClient(socketClient, ClientAdress):
    for i in range(3):
        req = socketClient.recv(1024)

        print(f"{ClientAdress}>> A requisição {i+1} foi {req.decode()}")

        rep = "Mensagem recebida!"

        socketClient.send(rep.encode())
    socketClient.close()
    print(f"Conexão finalizada com Cliente de addr {ClientAdress}.")

while True:
    print("Servidor esperando requisições")

    socketClient, ClientAdress = serverSocket.accept()

    print(f"Cliente com addr {ClientAdress} estabeleceu a comunicação")

    Thread(target=handleClient,args=[socketClient, ClientAdress]).start() 

    