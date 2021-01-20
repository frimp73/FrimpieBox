import os
from threading import Timer


class ShutdownScheduler:
    checkIdleInterval = 10.0 # Sekunden
    shutdownCommand = "sudo shutdown -h now"

    # shutdownTime in Minuten
    def __init__(self, mp3_player, shutdown_time, speaker_handler):
        self.mp3Player = mp3_player
        self.speakerHandler = speaker_handler
        if shutdown_time != 0:
            self.idleCounter = 0
            self.shutdownIdleCounter = shutdown_time * 60 / self.checkIdleInterval
            print("shutdown after " + str(shutdown_time) + " minutes")
            self._set_timer()

    def shutdown(self):
        if self.timer.is_alive():
            self.timer.cancel()

    def _set_timer(self):
        self.timer = Timer(self.checkIdleInterval, self._check_idle_state)
        self.timer.start()

    def _check_idle_state(self):
        if self.mp3Player.is_playing():
            self.idleCounter = 0
        else:
            if self.idleCounter == 0:
                self.speakerHandler.speaker_off()
            self.idleCounter = self.idleCounter + 1

        if self.idleCounter >= self.shutdownIdleCounter:
            os.system(self.shutdownCommand)
        else:
            self._set_timer()
 
