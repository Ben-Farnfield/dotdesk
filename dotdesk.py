#! /usr/bin/python

'''

'''

import shutil

from model.dot_desk_model import DotDeskModel
from util import util
from util import const
from view import view

# Install .desktop ------------------------------------------------------------

def install(args):

    program = args.i

    does_dotdesk_exist = util.make_does_dotdesk_exist(program)
    does_dotdesk_exist(const.GLOBAL_DESK_DIR) # exit if .desktop exists
    does_dotdesk_exist(const.LOCAL_DESK_DIR)

    dotdesk = DotDeskModel(program)

    dotdesk = run_install_cli(dotdesk)

    #DEBUG
    print dotdesk
    print "icon_to_install=" + dotdesk.icon_to_install

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

            dir_names = util.get_dirs(const.ICON_THEME) # get icon size list
            num_sizes = len(dir_names) # get number of icon sizes available

            print "Available icon sizes:"
            view.print_list(dir_names) # print all icon sizes
            select = view.prompt_select("Select 0-" + str(num_sizes-1),
                                        "Selection not available.",
                                        num_sizes)
            icon_size = dir_names[select]
            dotdesk.icon = (const.GLOBAL_ICON_DIR.format(size=icon_size) 
                            + icon_name)
        else:
            dotdesk.icon = const.LOCAL_ICON_DIR + icon_name

    dotdesk.exe = view.prompt_string("Enter execution command")

    print "Available categories:"
    view.print_list(const.CATEGORIES_LIST) # print all categories
    num_cat = len(const.CATEGORIES_LIST)
    select = view.prompt_select("Select 0-" + str(num_cat-1),
                                "Selection not available.",
                                num_cat)
    dotdesk.category = const.CATEGORIES_LIST[select]

    return dotdesk


def run_install_icon(dotdesk):
    icon_name = util.extract_file_name_from_path(dotdesk.icon_to_install)
    print "Installing icon " + icon_name
    shutil.copyfile(dotdesk.icon_to_install, dotdesk.icon)


def run_install_desktop(dotdesk):
    prog_name = dotdesk.name
    print "Installing " + prog_name + ".desktop"
    
    if util.is_root_install():
        install_dir = const.GLOBAL_DESK_DIR
    else:
        install_dir = const.LOCAL_DESK_DIR
        
    desktop = open(install_dir + prog_name + ".desktop", "w")
    desktop.write(str(dotdesk))
    desktop.close()

#~ def install_icons(args):
    #~ icon_name = (PROG+"."+args.install)
    #~ for i in range(len(ICON_SIZES)):
        #~ print ("Installing "+ICON_SIZES[i]+" "+icon_name)
        #~ shutil.copyfile((WRK_DIR+"/icons/"+ICON_SIZES[i]+"/"+icon_name), 
                        #~ (ICON_INST_HOME+"/"+ICON_SIZES[i]+"/apps/"+icon_name))
#~ 
#~ 
#~ def remove_icons():
    #~ for i in range(len(ICON_SIZES)):
        #~ for j in range(len(ICON_TYPES)):
            #~ icon_path = (ICON_INST_HOME+"/"+ICON_SIZES[i]+"/apps/"
                         #~ +PROG+"."+ICON_TYPES[j])
            #~ if os.path.isfile(icon_path):
                #~ print ("Removing "+ICON_SIZES[i]+" "+PROG+"."+ICON_TYPES[j])
                #~ os.remove(icon_path)
#~ 
#~ 
#~ def install_desktop(args):
    #~ print "Installing .desktop file"
    #~ desktop = open("/usr/share/applications/"+PROG+".desktop", "w")
    #~ desktop.write(get_desktop_contents(args))
    #~ desktop.close()
#~ 
#~ 
#~ def remove_desktop():
    #~ print "Removing .desktop file"
    #~ os.remove("/usr/share/applications/"+PROG+".desktop")


# Remove .desktop -------------------------------------------------------------

def remove():
    run_remove_icon()
    run_remove_desktop()


def run_remove_icon():
    pass


def run_remove_desktop():
    pass


# Main ------------------------------------------------------------------------

_args = util.get_args()

if _args.i:
    install(_args)
elif _args.r:
    remove()
else:
    print "Try 'setup.py --help'"

# -----------------------------------------------------------------------------
