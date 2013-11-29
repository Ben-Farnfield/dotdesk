
'''

'''

import getpass

# Current users home directory.
HOME = "/home/" + getpass.getuser() + "/"


# Default icon theme for global install.
ICON_THEME = "/usr/share/icons/hicolor/"


# Icon install directories.
GLOBAL_ICON_DIR = ICON_THEME + "{icon_size}/apps/"
LOCAL_ICON_DIR = HOME + ".icons/"


# .desktop install directories.
GLOBAL_DESK_DIR = "/usr/share/applications/"
LOCAL_DESK_DIR = HOME + ".local/share/applications/"


# Icon types supported.
ICON_TYPES = [".png", ".svg", ".ico"]


# List of all available program categories.
CATEGORIES_LIST = ["AudioVideo",
                   "Audio",
                   "Video",
                   "Development",
                   "Education",
                   "Game",
                   "Graphics",
                   "Network",
                   "Office",
                   "Science",
                   "Settings",
                   "System",
                   "Utility"]
