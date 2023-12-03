import socket
import threading
import room

# Choosing Nickname
nickname = input("Choose your nickname: ")
room_message = input(room.input_room_message)

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode("utf8")
            if message == "NICK":
                client.send(nickname.encode("utf8"))
            elif message == "ROOM":
                client.send(room_message.encode("utf8"))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        message = "{}: {}".format(nickname, input(""))
        client.send(message.encode("utf8"))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
