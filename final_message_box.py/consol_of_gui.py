import socket
from _thread import *
from tkinter import *



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",1025))
server.listen(10)

all_client = []


def tasking(client):
    while True:
        try:
            a = client.recv(3096)
            for c in all_client:
                c.send(a)

        except:
            print("task problem")
            break





def connecting():
    global all_client
    while True:
        try:
            client,add = server.accept()
            print(f"{add} joined the server")
            print("hii")
            all_client.append(client)
            start_new_thread(tasking,(client,))
            
        except:
            print("Connection not established")
            break
connecting()




