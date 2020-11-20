from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

BUFSIZ = 512
HOST = 'localhost'
PORT = 5550
ADDR = (HOST, PORT)

persons = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def broadcast(msg, name):
    for person in persons:
        client = person.client
        client.send(bytes(name, "utf8") + msg)

def client_communication(person):
    client = person.client
    addr = person.addr

    name = client.recv(BUFSIZ).decode("utf8")
    person.set_name(name)
    msg = bytes(f"{name} has joined the chat!", "utf8")
    broadcast(msg, "")

    while True:
        try:
            msg = client.recv(BUFSIZ)

            if msg == bytes("{quit}", "utf8"):
                # client.send(bytes("{quit}", "utf8"))
                client.close()
                persons.remove(person)
                broadcast(bytes(f"{name} has left the chat", "utf8"), "")
                print(f"[DISCONNECTED] {name} disconnected")
                break
            else:
                broadcast(msg, name + ": ")
                print(f"{name} :", msg.decode("utf8"))
        except Exception as e:
            print("[EXCEPTION]", e)
            break

def wait_for_connection():
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[EXCEPTION]", e)
            run = False

    print("SERVER CRASH")



if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
