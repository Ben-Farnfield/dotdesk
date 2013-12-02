
'''

'''

import utils
import const

import sys

def install(args):
    program = args.i
    
    if utils.file_exists(const.DESK_INSTALL_DIR + program + ".desktop"):
        print program + ".desktop is already installed."
        sys.exit()

    


# cli
# check if desktop installed DONE
# > ask if terminal app?
# > ask for tooltip
# > ask for exec cmnd
# > ask for category
# > ask if install icon?
# > enter full path to icon.
# extract icon format
# check if format supported
# > ask icon size.
