import os


class FolderHandler:

    def __init__(self, base_path):
        self.basePath = base_path

    def get_folder_by_tag(self, tag):
        if tag == "":
            return ""

        tag_folder = tag
        tag_folder_path = os.path.join(self.basePath, tag_folder)
        if os.path.exists(tag_folder_path):
            return tag_folder

        for entry in os.listdir(self.basePath):
            if not entry.isdigit():
                entry_path = os.path.join(self.basePath, entry)
                print entry_path
                if os.path.isdir(entry_path):
                    os.rename(entry_path, tag_folder_path)
                    return tag_folder
        return ""
