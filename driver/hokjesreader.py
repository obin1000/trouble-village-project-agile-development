import RPi.GPIO as GPIO

import time


class Resources:
    hout1 = 7
    hout2 = 3
    hout3 = 5

    water1 = 13
    water2 = 11
    water3 = 15
    #Constructor for basic gpio settings
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        #Needed pins to in/output with pull-up/pull-down resistor if needed
        #pins for the touch sensors
        GPIO.setup(Resources.hout1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Resources.hout2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Resources.hout3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(Resources.water1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Resources.water2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(Resources.water3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #Enable interrupts for touch sensors
        GPIO.add_event_detect(Resources.hout1, GPIO.BOTH, callback=self.eenOfAndereCallback)
        GPIO.add_event_detect(Resources.hout2, GPIO.BOTH, callback=self.eenOfAndereCallback)
        GPIO.add_event_detect(Resources.hout3, GPIO.BOTH, callback=self.eenOfAndereCallback)

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
        Occupied = [GPIO.input(Resources.hout1), GPIO.input(Resources.hout2), GPIO.input(Resources.hout3), GPIO.input(Resources.water1), GPIO.input(Resources.water2), GPIO.input(Resources.water3)]
        return Occupied
