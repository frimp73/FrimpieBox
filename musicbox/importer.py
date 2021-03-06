import os
from shutil import copytree


class Importer:
    importPath = "/media/usb/"

    def __init__(self, base_path):
        self.basePath = base_path

    def new_music_available(self):
        import_folder_content = os.listdir(self.importPath)
        return len(import_folder_content) > 0
        
    def import_new_music(self, tag):
        new_music_path = os.path.join(self.basePath, tag)
        copytree(self.importPath, new_music_path)
        os.system("sudo chown -R pi " + new_music_path)
        
