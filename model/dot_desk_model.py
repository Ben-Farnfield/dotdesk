class DotDeskModel(object):
    '''
    This class models the .desktop file to be installed.
    '''
    def __init__(self, name=None):
        self.name = name
        self.tooltip = None
        self.terminal = None
        self.icon = None
        self.exe = None
        
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
