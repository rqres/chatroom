from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from time import sleep

HOST = 'localhost'
PORT = 5550
ADDR = (HOST, PORT)
BUFSIZ = 512

messages = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

def receive_messages():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode()
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION]", e)
            break

def send_message(msg):
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()

receive_thread = Thread(target=receive_messages)
receive_thread.start()

send_message("Rares")
sleep(5)
send_message("disjoad")
sleep(2)
send_message("{quit}")
