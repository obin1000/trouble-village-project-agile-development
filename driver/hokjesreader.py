import RPi.GPIO as GPIO


class Resources:
    hout1 = 7
    hout2 = 3
    hout3 = 5

    water1 = 13
    water2 = 11
    water3 = 15

    rood1 = 37
    rood2 = 35
    rood3 = 33

    blauw1 = 40
    blauw2 = 38
    blauw3 = 36
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

        GPIO.setup(Resources.rood1, GPIO.OUT)
        GPIO.setup(Resources.rood2, GPIO.OUT)
        GPIO.setup(Resources.rood3, GPIO.OUT)

        GPIO.setup(Resources.blauw1, GPIO.OUT)
        GPIO.setup(Resources.blauw2, GPIO.OUT)
        GPIO.setup(Resources.blauw3, GPIO.OUT)

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
            if channel == Resources.hout1:
                GPIO.output(Resources.rood1, GPIO.LOW)
            elif channel == Resources.hout2:
                GPIO.output(Resources.rood2, GPIO.LOW)
            elif channel == Resources.hout3:
                GPIO.output(Resources.rood3, GPIO.LOW)
            elif channel == Resources.water1:
                GPIO.output(Resources.blauw1, GPIO.LOW)
            elif channel == Resources.water2:
                GPIO.output(Resources.blauw2, GPIO.LOW)
            elif channel == Resources.water3:
                GPIO.output(Resources.blauw3, GPIO.LOW)
        else:
            print("falling edge detected on" + str(channel))
            if channel == Resources.hout1:
                GPIO.output(Resources.rood1, GPIO.HIGH)
            elif channel == Resources.hout2:
                GPIO.output(Resources.rood2, GPIO.HIGH)
            elif channel == Resources.hout3:
                GPIO.output(Resources.rood3, GPIO.HIGH)
            elif channel == Resources.water1:
                GPIO.output(Resources.blauw1, GPIO.HIGH)
            elif channel == Resources.water2:
                GPIO.output(Resources.blauw2, GPIO.HIGH)
            elif channel == Resources.water3:
                GPIO.output(Resources.blauw3, GPIO.HIGH)

    def getOccupiedResources(self):
        Occupied = [GPIO.input(Resources.hout1), GPIO.input(Resources.hout2), GPIO.input(Resources.hout3), GPIO.input(Resources.water1), GPIO.input(Resources.water2), GPIO.input(Resources.water3)]
        return Occupied
