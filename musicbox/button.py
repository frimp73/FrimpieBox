import RPi.GPIO as GPIO
import time
import thread


class Button:

    def __init__(self, pin, callback):
        self.callback = callback
	GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.add_event_detect(pin, GPIO.FALLING, callback=self._measure, bouncetime = 300)

    def _measure(self, pin):
	thread.start_new_thread(self._check_if_button_is_still_pressed, (pin, ))

    def _check_if_button_is_still_pressed(self, pin):
	time.sleep(0.1)
	if GPIO.input(pin) == 0:
	    self.callback(pin)
