from gpiozero import LED
from time import sleep



led_red = LED(2)
led_white = LED(4)
led_green = LED(17)

while True:
    led_red.on()
    sleep(5)
    led_red.off()


    led_white.on()
    sleep(5)
    led_white.off()

    led_green.on()
    sleep(5)
    led_green.off()
