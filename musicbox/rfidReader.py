from time import sleep
import MFRC522


class RFIDReader:

    def __init__(self):
        self.last_tag = ""
        self.reader = MFRC522.MFRC522()

    def wait_for_tag_change(self, old_tag):
        self.last_tag = old_tag
        if self.last_tag == "":
            tag = self._wait_for_tag()
            self.last_tag = tag
        else:
            self.last_tag = self._wait_until_tag_removed(self.last_tag)
        return self.last_tag

    def antenna_off(self):
        print("Antenna Off")
        self.reader.AntennaOff()

    def _wait_for_tag(self):
        status = self.reader.MI_ERR
        while status != self.reader.MI_OK:
            (status,TagType) = self.reader.MFRC522_Request(self.reader.PICC_REQIDL)
            if status != self.reader.MI_OK:
                sleep(1)
        # Card is found - get the UID of the card
        return self._read_tag()

    def _wait_until_tag_removed(self, tag):
        status = self.reader.MI_OK
        new_tag = tag
        while (status == self.reader.MI_OK) & (tag == new_tag):
            # beim ersten mal kommt Status 2
            self.reader.MFRC522_Request(self.reader.PICC_REQIDL)
            # beim 2. mal Status 0 - aber so funktioniert's
            sleep(1)
            (status, TagType) = self.reader.MFRC522_Request(self.reader.PICC_REQIDL)
            if status == self.reader.MI_OK:
                new_tag = self._read_tag()
        if status != self.reader.MI_OK:
            # Card is removed
            new_tag = ""
        return new_tag

    def _read_tag(self):
        (status, uid) = self.reader.MFRC522_Anticoll()
        tag = "".join(str(e) for e in uid)
        return tag