from gpiozero import Button, Buzzer
from time import sleep

#switch variable pin no 2
switch = Button(2)

#buzzer variable pin no 16
buzzer = Buzzer(16)

#buzzer function that plays buzzer in pattren
def buzzerBeep():
    buzzer.beep(0.05,0.05,5, False)
    sleep(0.3)
    buzzer.beep(0.3,0.3,2, False)
    sleep(0.3)
    buzzer.beep(0.05,0.05,5, False)

#call "buzzerBeep" function when switch release
#switch.when_released = buzzerBeep
while True:
    if switch.is_pressed:
        buzzerBeep()
