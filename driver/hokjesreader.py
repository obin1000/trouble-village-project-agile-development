import RPi.GPIO as GPIO

import time


class Resources:
    wood1 = 3
    wood2 = 5
    wood3 = 7

    water1 = 11
    water2 = 13
    water3 = 15
    #Constructor for basic gpio settings
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        #SNeeded pins to in/output with pull-up/pull-down resistor if needed
        #pins for the touch sensors ikr
        GPIO.setup(Resources.wood1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Resources.wood2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Resources.wood3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(Resources.water1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Resources.water2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Resources.water3, GPIO.IN, pull_up_down=GPIO.PUD_UP)


        #pins for the leds


        #Enable interrupts for touch sensors
        GPIO.add_event_detect(Resources.wood1, GPIO.BOTH, callback=self.eenOfAndereCallback)
        GPIO.add_event_detect(Resources.wood2, GPIO.BOTH, callback=self.eenOfAndereCallback)
        GPIO.add_event_detect(Resources.wood3, GPIO.BOTH, callback=self.eenOfAndereCallback)

        GPIO.add_event_detect(Resources.water1, GPIO.BOTH, callback=self.eenOfAndereCallback)
        GPIO.add_event_detect(Resources.water2, GPIO.BOTH, callback=self.eenOfAndereCallback)
        GPIO.add_event_detect(Resources.water3, GPIO.BOTH, callback=self.eenOfAndereCallback)


    def eenOfAndereCallback(self, channel):
        #condition to seperate rising form falling
        if GPIO.input(channel):
            print("rising edge detected on" + str(channel))
            if channel == 36:
                GPIO.output(7, GPIO.LOW)
            elif channel == 38:
                GPIO.output(11, GPIO.LOW)
            elif channel == 40:
                GPIO.output(13, GPIO.LOW)
            elif channel == 33:
                GPIO.output(12, GPIO.LOW)
            elif channel == 35:
                GPIO.output(16, GPIO.LOW)
            elif channel == 37:
                GPIO.output(18, GPIO.LOW)
        else:
            print("falling edge detected on" + str(channel))
            if channel == 36:
                GPIO.output(7, GPIO.HIGH)
            elif channel == 38:
                GPIO.output(11, GPIO.HIGH)
            elif channel == 40:
                GPIO.output(13, GPIO.HIGH)
            elif channel == 33:
                GPIO.output(12, GPIO.HIGH)
            elif channel == 35:
                GPIO.output(16, GPIO.HIGH)
            elif channel == 37:
                GPIO.output(18, GPIO.HIGH)

    def getOccupiedResources(self):
        Occupied = [GPIO.input(Resources.wood1), GPIO.input(Resources.wood2), GPIO.input(Resources.wood3), GPIO.input(Resources.water1), GPIO.input(Resources.water2), GPIO.input(Resources.water3)]
        return Occupied


kno = Resources()
i = 0
while True:
    print("aww yies boy " + str(i))
    i += 1
    time.sleep(2)
    for occu in kno.getOccupiedResources():
        print(occu)
