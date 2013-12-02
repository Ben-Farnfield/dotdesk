
'''

'''

import utils
import const
import interface.prompt
import interface.output
from model.dot_desktop_model import DotDesktopModel

import sys

def install(args):
    icon_to_install = None
    icon_type = None
    icon_size = None

    program = args.i
    
    if utils.file_exists(const.DESK_INSTALL_DIR + program + ".desktop"):
        print program + ".desktop is already installed."
        sys.exit()

    desktop = DotDesktopModel(program)
    desktop = run_install_cli(desktop)
    run_icon_install(desktop)
    run_desktop_install(desktop)

def run_install_cli(desktop):
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
        
    return desktop

def run_icon_install():
    pass

def run_desktop_install():
    pass
