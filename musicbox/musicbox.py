from folderHandler import FolderHandler
from rfidReader import RFIDReader
from mp3Player import MP3Player
from speakerHandler import SpeakerHandler
from buttonHandler import ButtonHandler
from importer import Importer
from settings import Settings
from shutdownScheduler import ShutdownScheduler

base_path = "/home/pi/musicbox/"
music_path = base_path + "music"
shutdown_time = 30 # shutdown after 30 minutes

settings = Settings(base_path)
speaker_handler = SpeakerHandler()
mp3_player = MP3Player(music_path, settings, speaker_handler)
button_handler = ButtonHandler(mp3_player)
folder_handler = FolderHandler(music_path)
importer = Importer(music_path)
rfid_reader = RFIDReader()
shutdown_scheduler = ShutdownScheduler(mp3_player, rfid_reader, shutdown_time)

tag = ""
while True:
    tag = rfid_reader.wait_for_tag_change(tag)
    if tag == "":
        print tag + " removed."
        mp3_player.pause()
    else:
        print str(tag) + " detected."
        folder = folder_handler.get_folder_by_tag(tag)
        if folder != "":
            mp3_player.play(folder)
        else:
            print "Tag is new..."
            if importer.new_music_available():
                print "New music for import found."
                folder = str(tag)
                importer.import_new_music(folder)
                mp3_player.play(folder)
            else:
                print "No folder assigned."

