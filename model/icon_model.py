import const

class IconModel(object):
    ''' This class models the icon to be installed. '''
    def __init__(self, name=""):
        self.program_name = name
        self.icon_type = ""
        self.icon_size = ""
        self.icon_to_install = ""

    def __str__(self):
        # put assert in here !
        install_dir = const.ICON_INSTALL_DIR.format(icon_size=self.icon_size)
        icon_name = self.program_name + self.icon_type
        
        return install_dir + icon_name
