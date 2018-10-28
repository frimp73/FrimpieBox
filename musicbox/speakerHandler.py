import RPi.GPIO as GPIO


class SpeakerHandler:
    mutePin = 3
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.mutePin, GPIO.OUT, initial = 0)
        GPIO.output(self.mutePin, 1)

    def speakerOff(self):
        GPIO.output(self.mutePin, 1)

    def speakerOn(self):
        GPIO.output(self.mutePin, 0)
