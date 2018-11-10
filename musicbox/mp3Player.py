import os
from subprocess import Popen, PIPE


class MP3Player:
    volumeSteps = 5
    last_played_folder = ""
    playerPath = "/usr/bin/mocp"
    startPlayer = playerPath + " -S"
    playCommand = playerPath + " --playit"
    stopCommand = playerPath + " --stop"
    pauseCommand = playerPath + " --pause"
    continueCommand = playerPath + " --unpause"
    nextCommand = playerPath + " --next"
    previousCommand = playerPath + " --previous"
    volumeCommand = playerPath + " --volume="
    infoCommand = "--info"

    def __init__(self, base_path, settings, speaker_handler):
        self.basePath = base_path
        self.settings = settings
        self.volume = settings.volume
        self.speakerHandler = speaker_handler
        # initialize mocp server
        os.system(self.startPlayer)
        self._set_volume()

    def play(self, folder):
        self.speakerHandler.speaker_on()
        if (folder != self.last_played_folder) | self.is_stopped():
            print "Start player (" + folder + ")..."
            self.last_played_folder = folder
            folder_path = os.path.join(self.basePath, folder, "*")
            os.system(self.playCommand + " " + folder_path)
        else:
            print "Continue " + folder + "..."
            os.system(self.continueCommand)

    def stop(self):
        print "Stop player..."
        os.system(self.stopCommand)
        self.speakerHandler.speaker_off()

    def pause(self):
        print "Pause player..."
        os.system(self.pauseCommand)
        self.speakerHandler.speaker_off()

    def next(self):
        print "Next track..."
        os.system(self.nextCommand)
        # if there's nothing more to play, switch speaker off
        if self.is_stopped():
            self.speakerHandler.speaker_off()


    def previous(self):
        print "Previous track..."
        os.system(self.previousCommand)
        # if there's nothing more to play, switch speaker off
        if self.is_stopped():
            self.speakerHandler.speaker_off()

    def volume_up(self):
        if self.volume <= (100 - self.volumeSteps):
            self.volume += self.volumeSteps
        self._set_volume()

    def volume_down(self):
        if self.volume >= self.volumeSteps:
            self.volume -= self.volumeSteps
        self._set_volume()

    def is_stopped(self):
        p = Popen([self.playerPath,"--info"], stdout=PIPE)
        output = p.communicate()
        return output[0].startswith("State: STOP")

    def is_playing(self):
        p = Popen([self.playerPath,"--info"], stdout=PIPE)
        output = p.communicate()
        return output[0].startswith("State: PLAY")

    def _set_volume(self):
        print "Volume " + str(self.volume)
        os.system(self.volumeCommand + str(self.volume))
        self.settings.store_volume(self.volume)
