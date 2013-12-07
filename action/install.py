
"""
This module controls the install process for dotdesk.

install() -- runs the full install process
"""

import utils
import const
from interface import prompt
from interface import output
from model.dot_desktop_model import DotDesktopModel
from model.icon_model import IconModel

import sys

def install(args):
    """ Runs full install process if the .desktop file doesn't exist. """
    program = args["name"]

    if utils.file_exists(DotDesktopModel.INSTALL_DIR + program + ".desktop"):
        print program + ".desktop is already installed."
        sys.exit()

    desktop = DotDesktopModel(program)
    icon = IconModel(program)

    desktop, icon = _run_install_cli(desktop, icon)

    output.line() # make things pretty
    
    _run_desktop_install(desktop)

    if icon.install_icon:
        _run_icon_install(icon)
        
    print "Bye!"
    output.line()


def _run_install_cli(desktop, icon):
    """ 
    Runs the full install interface.
    
    The user is asked for all the basic info a .desktop file requires. The
    user is provided the option to install an icon or not.
    """
    desktop.terminal = prompt.for_yes_no("Terminal app?")
    desktop.tooltip = prompt.for_string("Enter tooltip")
    desktop.exe = prompt.for_string("Enter execution command")

    output.option_list("Select a category", const.CATEGORIES)
    selection = prompt.for_selection("Make a selection", const.CATEGORIES_LEN)
    desktop.category = const.CATEGORIES[selection]

    icon.install_icon = prompt.for_yes_no("Install an icon?")
    if icon.install_icon:
        icon.icon_to_install = prompt.for_path("Enter full path to icon")
        icon.icon_type = utils.file_type(icon.icon_to_install)

        output.option_list("Select icon size", const.ICON_SIZES)
        selection = prompt.for_selection("Make a selection",
                                         const.ICON_SIZES_LEN)
        icon.icon_size = const.ICON_SIZES[selection]

        desktop.icon = str(icon)

    return desktop, icon


def _run_desktop_install(desktop):
    """ Installs the .desktop file in its install dir. """
    path = DotDesktopModel.INSTALL_DIR + desktop.name + ".desktop"
    desktop_contents = str(desktop)
    utils.proc_file("write", path, desktop_contents,
                     desktop.name + ".desktop installed!",
                     "!!Issue installing .desktop!!")


def _run_icon_install(icon):
    """ Installs the icon in its install dir. """
    install_path = str(icon)
    utils.proc_file("copy", icon.icon_to_install, install_path,
                    icon.icon_name + icon.icon_type + " installed!",
                    "!!Issue installing icon!!")
