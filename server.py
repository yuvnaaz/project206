import socket
from threading import Thread

port = 6000
ip = '127.0.0.1'
server = None
clients = {}

def setup():
    global ip
    global server
    global port
    print("Welcome to Tembula game!")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(10)
    print("Server is waiting for connections...")

def acceptConnections():
    global clients
    global server

    while True:
        playerSocket, addr = server.accept()
        playerName = playerSocket.recv(1024).decode().strip()
        print(f"Connection found with {playerName}: {addr}")
        if not clients:
            clients[playerName] = {'player_type': 'player1'}
        else: 
            clients[playerName] = {'player_type': 'player2'}

        clients[playerName]["playerSocket"] = playerSocket
        clients[playerName]["address"] = addr
        clients[playerName]["playerName"] = playerName
        clients[playerName]["turn"] = False

if __name__ == "__main__":
    setup()
    Thread(target=acceptConnections).start()
