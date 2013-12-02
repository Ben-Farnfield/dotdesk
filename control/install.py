
'''

'''

import utils
import const
import interface.prompt
import interface.output
from model.dot_desktop_model import DotDesktopModel

import sys

def install(args):
    program = args.i
    
    if utils.file_exists(const.DESK_INSTALL_DIR + program + ".desktop"):
        print program + ".desktop is already installed."
        sys.exit()

    desktop = DotDesktopModel(program)

    desktop.terminal = prompt.for_yes_no("Terminal app?")
    desktop.tooltip = prompt.for_string("Enter tooltip")
    desktop.exe = prompt.for_string("Enter execution command")

    
    desktop.category = 

# cli
# check if desktop installed DONE
# > ask if terminal app? DONE
# > ask for tooltip DONE
# > ask for exec cmnd DONE
# > ask for category
# > ask if install icon?
# > enter full path to icon.
# extract icon format
# check if format supported
# > ask icon size.
