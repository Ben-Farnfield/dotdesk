
'''

'''

from model.dot_desktop_model import DotDesktopModel
from model.icon_model import IconModel
import utils
import const

def remove(args):
    program = args.r

    if not utils.file_exists(DotDesktopModel.INSTALL_DIR + program + ".desktop"):
        print program + ".desktop is not installed."
        sys.exit()
    
    _run_remove_desktop(program)
    _run_remove_icon(program)

def _run_remove_desktop(program):
    utils.remove_file(DotDesktopModel.INSTALL_DIR + program + ".desktop",
                      "\n.desktop removed!",
                      "\n!!Issue removing .desktop!!")

def _run_remove_icon(program):
    for icon_size in const.ICON_SIZES:
        tmp_dir = IconModel.INSTALL_DIR.format(icon_size=icon_size)
        for icon_type in const.ICON_TYPES:
            tmp_path = tmp_dir + program + icon_type
            if utils.file_exists(tmp_path)
                utils.remove_file(tmp_path)
                return
