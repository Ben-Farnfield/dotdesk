
__author__ = "Ben Farnfield"
__email__ = "ben.farnfield@gmail.com"

__license__ = ""


class DotDeskModel:

    '''
    This class models the .desktop file to be installed.
    '''

    def __init__(self, name=""):
        self.name = name
        self.tooltip = ""
        self.terminal = ""
        self.icon = ""
        self.exe = ""
        
    def to_string(self):
        return ("[Desktop Entry]\n" +
        "Version=1.0\n" +
        "Type=Application\n" + 
        "Encoding=UTF-8\n" +
        "Name=" + self.name + "\n" +
        "Comment=" + self.tooltip + "\n" +
        "Icon=" + self.icon + "\n" +
        "Exec=" + self.exe + "\n" +
        "Terminal=" + str(self.terminal) + "\n" +
        "Categories=TBC")
