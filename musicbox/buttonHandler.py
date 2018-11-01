import RPi.GPIO as GPIO
from button import Button

class ButtonHandler:
    volumeUpPin = 40
    volumeDownPin = 35
    nextPin = 38
    previousPin = 37

    def __init__(self, mp3_player):
        self.mp3Player = mp3_player
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        Button(self.volumeUpPin, self._button_pressed)
        Button(self.volumeDownPin, self._button_pressed)
        Button(self.nextPin, self._button_pressed)
        Button(self.previousPin, self._button_pressed)

    def _button_pressed(self, button):
        if button == self.volumeUpPin:
            print "Volume +"
            self.mp3Player.volume_up()
        elif button == self.volumeDownPin:
            print "Volume -"
            self.mp3Player.volume_down()
        elif button == self.nextPin:
            print "Next"
            self.mp3Player.next()
        elif button == self.previousPin:
            print "Previous"
            self.mp3Player.previous()
