
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

    output.option_list("Select a category", const.CATEGORIES)
    selection = prompt.for_selection("Make selection", const.CATEGORIES_LEN)
    desktop.category = const.CATEGORIES[selection]

    install_icon = prompt.for_yes_no("Install an icon?")
    if install_icon:
        icon_to_install = prompt.for_path("Enter full path to icon")
        icon_type = utils.file_type(icon_to_install)

        output.option_list("Select an icon size", const.ICON_SIZES)
        selection = prompt.for_selection("Make selection",
                                         const.ICON_SIZES_LEN)
        icon_size = const.ICON_SIZES[selection]

# cli
# check if desktop installed DONE
# > ask if terminal app? DONE
# > ask for tooltip DONE
# > ask for exec cmnd DONE
# > ask for category DONE
# > ask if install icon? DONE
# > enter full path to icon. DONE
# extract icon format DONE
# > ask icon size. DONE
