
'''

'''

import os
import sys

from util import util
from view import view

def remove(args):

    program = args.r

    run_remove_icon(program)
    run_remove_desktop(program)


def run_remove_icon(program):
    icon_types = const.ICON_TYPES
    
    if util.is_root_install():
        icon_path = const.GLOBAL_ICON_DIR + program + "{icon_type}"
        icon_sizes = util.get_dirs(const.ICON_THEME)
        for i in range(len(icon_sizes)):
            for j in range(len(icon_types)):
                tmp_path = icon_path.format(icon_size=icon_sizes[i],
                                            icon_type=icon_types[j])
                if util.file_exists(tmp_path):
                    os.remove(tmp_path)
                    return
    else:
        icon_path = const.LOCAL_ICON_DIR + program + "{icon_type}"
        for i in range(len(icon_types)):
            tmp_path = icon_path.format(icon_type=icon_types[i])
            if util.file_exists(tmp_path):
                os.remove(tmp_path)
                return

    if util.is_root_install():
        view.print_string("Icon not found!")
        sys.exit()
    else:
        view.print_string("Icon not found. Try running as 'root' user.")
        sys.exit()


def run_remove_desktop(program):

    if util.is_root_install():
        desk_path = const.GLOBAL_DESK_DIR + program + ".desktop"
        if util.file_exists(desk_path):
            os.remove(desk_path)
            return

    desk_path = const.LOCAL_DESK_DIR + program + ".desktop"
    if util.file_exists(desk_path):
        os.remove(desk_path)
        return
    else:
        if util.is_root_install():
            view.print_string(program + ".desktop not found!")
            sys.exit()
        else:
            view.print_string(program + ".desktop not found." +
                                        "Try running as 'root' user.")
            sys.exit()
