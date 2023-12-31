""" pmpermit configuration module """

PMPERMITDV = [
    "PMPERMIT",
    "PM_LIMIT",
    "PMPERMIT_PIC",
    "PMPERMIT_TEXT"
    ]




class PmpermitConfig(object):
    @property
    def Pmpermit(self):
        """ Check whether pmpermit is on | off """
        return self.getdv("PMPERMIT") or self.PMPERMIT or None


    @property
    def PmpermitLimit(self):
        """ Check the number of warns, defaults to 4 """
        return self.getdv("PM_LIMIT") or self.PM_LIMIT or 4


    @property
    def PmpermitPic(self):
        """ Check whether you have added a pic in your pmpermit or not """
        return self.getdv("PMPERMIT_PIC") or self.PMPERMIT_PIC or None


    @property
    def PmpermitText(self):
        """ Get the pmpermit text """
        return self.getdv("PMPERMIT_TEXT") or self.PMPERMIT_TEXT or None
