#! /usr/bin/python

from model.dot_desk_model import DotDeskModel
from view import view

import argparse
import getpass
import shutil
import sys
import os

# Install Dir's --------------------------------------------------------------

_home = "/home/" + getpass.getuser() + "/"

_global_icon_dir = "/usr/share/icons/hicolor/{size}/apps/"
_local_icon_dir = _home + ".icons/"

_global_desk_dir = "/usr/share/applications/"
_local_desk_dir = _home + ".local/share/applications/"

_icon_source = None
_icon_name = None

# ----------------------------------------------------------------------------

# Get arguments passed by user.
def get_args():
    parser = argparse.ArgumentParser(prog="dotdoc")
    parser.add_argument("-i", help="Install .desktop and icons.")
    #~ parser.add_argument("-r", action="store_true",
                        #~ help="Remove .desktop and icons")
    return parser.parse_args()

# Check to see if file is installed.
def file_exists(filename):
    return os.path.isfile(filename)

# Check to see if script has been run as root.
def is_global_install():
    return getpass.getuser() == "root"

# Install .desktop
def install(args):
    # Get program name.
    program = args.i
    # Check if .desktop has already been installed.
    if file_exists(_global_desk_dir + program + ".desktop"):
        print program + ".desktop is already installed!"
        sys.exit()
    else:
        # Create .desktop model.    
        dotdesk = DotDeskModel(program)

    dotdesk.tooltip = view.prompt_string("Enter tooltip")
    dotdesk.terminal = view.prompt_Y_n("Terminal app?")
    # Ask use if they wish to install an icon.
    install_icon = view.prompt_Y_n("Do you wish to install an icon?")
    # If they wish to install an icon prompt for icon path.
    if install_icon:
        while True:
            icon_path = view.prompt_string("Enter icon path")
            if file_exists(icon_path):
                _icon_source = icon_path
                split_path = _icon_source.split("/")
                _icon_name = split_path[len(split_path)-1]
                break
            else:
                print "Icon not found!"
    # If is root user prompt for icon size.
    if is_global_install():
        # List all the possible sizes.
        dir_names = view.output_dirs("/usr/share/icons/hicolor")
        # Ask user to select icon size.
        while True:
            prompt = "Select icon size 0 .. " + str(len(dir_names)-1)
            selection = int(view.prompt_string(prompt))
            if selection >= 0 and selection < len(dir_names):
                icon_size = dir_names[selection]
                dotdesk.icon = (_global_icon_dir.format(size=icon_size) 
                                + _icon_name)
                break
            else:
                print "Invalid selection!"
    else:
        dotdesk.icon = _local_icon_dir + _icon_name
    dotdesk.exe = view.prompt_string("Enter execution command")
    
    #DEBUG
    print dotdesk.to_string()

def generate_dot_desktop():
    pass


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

# -----------------------------------------------------------------------------

#_wrk_dir = os.getcwd()

_args = get_args()

if _args.i:
    install(_args)
#elif _args.r:
#    print "remove"
#elif _args.g:
#    print "generate"
else:
    print "Try 'setup.py --help'"
