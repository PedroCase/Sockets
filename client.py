from socket import socket, AF_INET, SOCK_STREAM

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1',12345))


for _ in range(3):
    data = input()

    clientSocket.send(data.encode())

    rep = clientSocket.recv(1024)

    print(f"Resposta do servidor: {rep.decode()}")
