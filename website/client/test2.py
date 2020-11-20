from client import Client
from threading import Thread, Lock
from time import sleep

c1 = Client("Rares")
c2 = Client("Briana")

def update_messages():
    msgs = []
    run = True
    while run:
        sleep(0.1)
        new_messages = c1.get_messages()
        msgs.extend(new_messages)
        for msg in new_messages:
            print(msg)
            if msg == "{quit}":
                run = False
                break

Thread(target=update_messages).start()

c1.send_message("Buna briana")
sleep(2)
c2.send_message("Buna rares")
sleep(2)
c1.send_message("ce faci")
sleep(1)
c2.send_message("bn u")
sleep(2)
c1.send_message("uite bn")

sleep(5)

c1.disconnect()
sleep(2)
c2.disconnect()
