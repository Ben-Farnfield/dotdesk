#! /usr/bin/python

import argparse
import getpass
import shutil
import sys
import os

# Install Dir's ---------------------------------------------------------------

_home = "/home/" + getpass.getuser() + "/"

_global_icon_dir = "/usr/share/icons/hicolor/{size}/apps/"
_local_icon_dir = _home + ".icons/"

_global_desk_dir = "/usr/share/applications/"
_local_desk_dir = _home + ".local/share/applications/"

# -----------------------------------------------------------------------------

# Get arguments passed by user.
def get_args():
    parser = argparse.ArgumentParser(prog="dotdoc")
    parser.add_argument("-i", help="Install .desktop and icons.")
    #~ parser.add_argument("-r", action="store_true",
                        #~ help="Remove .desktop and icons")
    #~ parser.add_argument("-g", 
                        #~ help=("Generate dotdoc directory. Pass your "
                              #~ "programs name as the argument"))
    return parser.parse_args()


def install(args):
    # Get program name.
    program = args.i
    # Check if .desktop has already been installed.
    if desk_installed(program):
        print program + ".desktop is already installed!"
        sys.exit()
    # Ask user to input a tooltip.
    tooltip = raw_input("Enter tooltip: ")
    # Ask user if program is a terminal application.
    terminal = read_Y_n("Terminal app? Y/n: ")
    # Ask user if they wish to install an icon.
    install_icon = read_Y_n("Do you wish to install an icon? Y/n: ")
    if install_icon:
        while True:
            icon_path = raw_input("Enter path to icon: ")
            if os.path.isfile(icon_path)
                # need to think about local vs global
                (__, dirnames, __) = os.walk().next()
            else:
                print "Icon not found!"
            
            
    print "Program: " + program
    print "Tooltip: " + tooltip
    print "Terminal: " + str(terminal)
    print "Install Icon: " + str(install_icon)
    print "Icon Path: " + icon_path


def desk_installed(program):
    return os.path.isfile(_global_desk_dir + program + ".desktop")


def read_Y_n(prompt):
    while True:
        Y_n = raw_input(prompt)
        if Y_n is "Y" or Y_n is "y":
            return True
        elif Y_n is "N" or Y_n is "n":
            return False
        else:
            print "You need to enter Y or n"


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
    print "install"
    install(_args)
elif _args.r:
    print "remove"
elif _args.g:
    print "generate"
else:
    print "Try 'setup.py --help'"
