import socket
from gpiozero import LED, Button
from time import sleep

r = LED(14)
g = LED(17)



def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
        return False

if is_connected():
    print("yes")
    g.on()
    r.off()
else:
    print("no")
    r.on()
    g.off()

