
'''

'''

import utils
import const
import interface.prompt
import interface.output
from model.dot_desktop_model import DotDesktopModel
from model.icon_model import IconModel

import sys

def install(args):
    program = args.i

    if utils.file_exists(DotDesktopModel.INSTALL_DIR + program + ".desktop"):
        print program + ".desktop is already installed."
        sys.exit()

    desktop = DotDesktopModel(program)
    icon = IconModel(program)

    desktop, icon = run_install_cli(desktop, icon)

    if icon.install_icon:
        run_icon_install(icon)

    run_desktop_install(desktop)


def run_install_cli(desktop, icon):
    desktop.terminal = prompt.for_yes_no("Terminal app?")
    desktop.tooltip = prompt.for_string("Enter tooltip")
    desktop.exe = prompt.for_string("Enter execution command")

    output.option_list("Select a category", const.CATEGORIES)
    selection = prompt.for_selection("Make selection", const.CATEGORIES_LEN)
    desktop.category = const.CATEGORIES[selection]

    icon.install_icon = prompt.for_yes_no("Install an icon?")
    if icon.install_icon:
        icon.icon_to_install = prompt.for_path("Enter full path to icon")
        icon.icon_type = utils.file_type(icon.icon_to_install)

        output.option_list("Select an icon size", const.ICON_SIZES)
        selection = prompt.for_selection("Make selection",
                                         const.ICON_SIZES_LEN)
        icon.icon_size = const.ICON_SIZES[selection]

    return (desktop, icon)


def run_icon_install(icon):
    if utils.copy_file(icon.icon_to_install, str(icon)):
        print "Icon installed!"
    else:
        print "Issue installing icon!"
        sys.exit()


def run_desktop_install(desktop):
    install_path = DotDesktopModel.INSTALL_DIR + desktop.name + ".desktop"
    if utils.write_file(install_path, str(desktop)):
        print ".desktop installed!"
    else:
        print "Issue installing .desktop!"
        sys.exit()
