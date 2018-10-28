class Settings:
    settingsFile = "settings"
    
    def __init__(self, basePath):
        self.settingsFile = basePath + self.settingsFile
        with open(self.settingsFile, "r") as text_file:
            self.volume = int(text_file.readline())
            text_file.close()
                
    def store_volume(self, volume):
        self.volume = volume
        self._store_values()

    def _store_values(self):
        with open(self.settingsFile, "w") as text_file:
            text_file.write(str(self.volume) + "\n")
            text_file.close()

    def get_volume(self):
        return self.volume
