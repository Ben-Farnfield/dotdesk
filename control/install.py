
'''

'''

import shutil

from model.dot_desk_model import DotDeskModel
from util import util
from util import const
from view import view

def install(args):

    program = args.i

    does_dotdesk_exist = util.make_does_dotdesk_exist(program)
    does_dotdesk_exist(const.GLOBAL_DESK_DIR) # exit if .desktop exists
    does_dotdesk_exist(const.LOCAL_DESK_DIR)

    dotdesk = DotDeskModel(program)

    dotdesk = run_install_cli(dotdesk)
    run_install_icon(dotdesk)
    run_install_desktop(dotdesk)


def run_install_cli(dotdesk):

    dotdesk.tooltip = view.prompt_string("Enter tooltip")
    dotdesk.terminal = view.prompt_Y_n("Terminal app?")

    yes_install_icon = view.prompt_Y_n("Install icon?")
    
    if yes_install_icon:
        dotdesk.icon_to_install = view.prompt_path("Enter icon path",
                                                   "Icon not found.")

        icon_name = util.extract_file_name_from_path(dotdesk.icon_to_install)

        if util.is_root_install(): # we need to know the icon size.

            icon_sizes = util.get_dirs(const.ICON_THEME)
            num_sizes = len(icon_sizes)

            view.print_string("\nSelect icon size:")
            view.print_list(icon_sizes)
            select = view.prompt_select("0-" + str(num_sizes-1),
                                        "Selection not available.",
                                        num_sizes)
            icon_size = icon_sizes[select]
            dotdesk.icon = (const.GLOBAL_ICON_DIR.format(icon_size=icon_size) 
                            + icon_name)
        else:
            dotdesk.icon = const.LOCAL_ICON_DIR + icon_name

    dotdesk.exe = view.prompt_string("Enter execution command")

    view.print_string("\nSelect a category:\n")
    view.print_list(const.CATEGORIES_LIST)
    num_cat = len(const.CATEGORIES_LIST)
    select = view.prompt_select("0-" + str(num_cat-1),
                                "Selection not available.",
                                num_cat)
    dotdesk.category = const.CATEGORIES_LIST[select]

    return dotdesk


def run_install_icon(dotdesk):
    if dotdesk.icon != "":
        icon_name = util.extract_file_name_from_path(dotdesk.icon_to_install)
        install_path = util.remove_filename_from_path(dotdesk.icon)
        view.print_string("Installing icon " + icon_name)
        shutil.copyfile(dotdesk.icon_to_install, install_path)


def run_install_desktop(dotdesk):
    prog_name = dotdesk.name
    view.print_string("Installing " + prog_name + ".desktop")
    
    if util.is_root_install():
        install_dir = const.GLOBAL_DESK_DIR
    else:
        install_dir = const.LOCAL_DESK_DIR

    desktop = open(install_dir + prog_name + ".desktop", "w")
    desktop.write(str(dotdesk))
    desktop.close()
