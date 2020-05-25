from gpiozero import LED, Button
from time import sleep
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import socket
#from buzzer import *

# PyMouse is use to move mouse point at specific position
m = PyMouse()
k = PyKeyboard()

#sleep(2)

# set pin to variables
switch = Button(2)
greenLed = LED(17)
redLed = LED(14)

#name of whom you want to call
name = "enter name here"

# return the length of given name
name_length = len(name)

# Default LED is off
greenLed.off()
redLed.off()



def checkInternet():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
        return False
try:    

    while True:
        
        if checkInternet():
            redLed.off()

            # If switch pressed make call
            if switch.is_pressed:
                print ("Doorbell Pressed")
                greenLed.on()

                # Click to close the popup
                m.click(855,234)
                sleep(0.5)

                # Remove Previous Text from text box
                m.click(984,407)
                sleep(0.5)
                
                # Click in the Duo text box
                m.click(637,408)

                # Type name of Duo contact
                k.type_string(name)

                # Hit Return to select contact
                k.tap_key('Return')
                sleep(2.5)

                # Click on Video Call button
                m.click(737,592)
                
                greenLed.off()

                # Blink Green Led 30 times
                greenLed.blink(0.6, 0.6, 30, False)

            else:
                greenLed.off()
                sleep(0.05)
        else:
            redLed.on()
finally:
    print("Finally")    
