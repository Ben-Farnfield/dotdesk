
"""
This module controls the removal process for dotdesk.

remove()  -- runs the full removal process
"""

from model.dot_desktop_model import DotDesktopModel
from model.icon_model import IconModel
from interface import output
import utils
import const

import sys

def remove(args):
    """ Runs the full removal process after ensuring the .desktop exists. """
    program = args["name"]

    if not utils.file_exists(DotDesktopModel.INSTALL_DIR+program+".desktop"):
        print program + ".desktop is not installed."
        sys.exit()

    output.line()
    
    _run_remove_desktop(program)
    _run_remove_icon(program)
    
    print "Bye!"
    output.line()

def _run_remove_desktop(program):
    """ Removes the .desktop file from its install dir. """
    utils.proc_file("remove", 
                    DotDesktopModel.INSTALL_DIR + program + ".desktop",
                    msg=program + ".desktop removed!",
                    error="!!Issue removing .desktop!!")

def _run_remove_icon(program):
    """
    Removes the icon from its install dir.

    Iterates through all possible icon sizes and formats until it
    finds a match. It then removes this file and returns.
    """
    for icon_size in const.ICON_SIZES:
        tmp_dir = IconModel.INSTALL_DIR.format(icon_size=icon_size)
        for icon_type in const.ICON_TYPES:
            tmp_path = tmp_dir + program + icon_type
            if utils.file_exists(tmp_path):
                utils.proc_file("remove", tmp_path,
                                msg=program + icon_type + " removed!",
                                error="!!Issue removing icon!!")
                return
