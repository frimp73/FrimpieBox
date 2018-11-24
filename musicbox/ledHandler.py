import RPi.GPIO as GPIO


class LedHandler:
    startingPin = 10  # on during startup  - box is starting
    readyPin = 11     # on after start up  - box is ready
    offPin = 12       # on after shut down - box is off

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        # startingPin was switched on in /boot/config.txt  -so we switch it off
        GPIO.setup(self.startingPin, GPIO.OUT, initial = 0)
        GPIO.setup(self.readyPin, GPIO.OUT, initial = 1) # box is ready
        GPIO.setup(self.offPin, GPIO.OUT, initial = 0)

    def shutdown(self):
        GPIO.output(self.readyPin, 0)
        GPIO.output(self.offPin, 1)
