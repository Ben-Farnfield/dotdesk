from const import ICON_INSTALL_DIR

class IconModel(object):
    ''' This class models the icon to be installed. '''
    def __init__(self, icon_name=""):
        self.install_icon = False

        self.icon_to_install = ""

        self.icon_name = icon_name
        self.icon_type = ""
        self.icon_size = ""

    def __str__(self):
        # put assert in here !
        install_dir = ICON_INSTALL_DIR.format(icon_size=self.icon_size)
        icon = self.icon_name + self.icon_type
        
        return install_dir + icon
