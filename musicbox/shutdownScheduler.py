import os
from threading import Timer


class ShutdownScheduler:
    checkIdleInterval = 10 # Sekunden
    shutdownCommand = "sudo shutdown -h now"

    # shutdownTime in Minuten
    def __init__(self, mp3_player, rfid_reader, shutdown_time):
        self.mp3Player = mp3_player
        self.rfidReader = rfid_reader
        if shutdown_time != 0:
            self.idleCounter = 0
            self.shutdownIdleCounter = shutdown_time * 60 / self.checkIdleInterval
            print "shutdown after " + str(shutdown_time) + " minutes"
            self._set_timer()

    def _set_timer(self):
        Timer(self.checkIdleInterval, self._check_idle_state, ()).start()

    def _check_idle_state(self):
        if self.mp3Player.is_playing():
            self.idleCounter = 0;
        else:
            self.idleCounter = self.idleCounter + 1

        if self.idleCounter >= self.shutdownIdleCounter:
            self.rfidReader.antenna_off()
            os.system(self.shutdownCommand)
        else:
            self._set_timer()
 