#!/bin/python3
import socket
import threading

import room

host = "127.0.0.1"
port = 5555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()

# Lists For Clients and Their  Rooms
rooms = [[] for _ in range(len(room.rooms) + 1)]
clients = {}


# Sending Messages To All Connected to room_id Clients
def broadcast(room_id: int, message: str):
    for client in rooms[room_id]:
        client.send(message)


# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(clients.get(client).get("room_id"), message)
        except:
            # Removing And Closing Clients
            room_id = clients[client].get("room_id")
            rooms[room_id].remove(client)
            nickname = clients[client].get("nickname")
            room_name = room.rooms[room_id]
            clients.pop(client)
            client.close()
            broadcast(
                room_id,
                "{} left room {}!".format(nickname, room_name).encode("utf-8"),
            )
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send("ROOM".encode("utf8"))
        room_id = int(client.recv(1024).decode("utf8"))
        # Request And Store Nickname
        client.send("NICK".encode("utf8"))
        nickname = client.recv(1024).decode("utf8")
        # Request And Store Room
        rooms[room_id].append(client)

        clients[client] = {"room_id": room_id, "nickname": nickname}

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast(
            room_id,
            "{} joined to room {}!".format(nickname, room.rooms[room_id]).encode(
                "utf8"
            ),
        )
        client.send("Connected to server!".encode("utf8"))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server if listening...")
receive()
