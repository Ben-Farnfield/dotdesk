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
    desktop_contents = []
    
    # Get program name.
    program = args.i
    # Check if .desktop has already been installed.
    if desk_installed(program):
        print program + ".desktop is already installed!"
        sys.exit()
    else:
        desktop_contents.append(program)
    
    desktop_contents = desktop_install_cli(desktop_contents)
    
    # DEBUG
    for i in range(len(desktop_contents)):
        print desktop_contents[i]


def desktop_install_cli(desktop_contents):
    # Ask user to input a tooltip.
    desktop_contents.append(raw_input("Enter tooltip: "))
    # Ask user if program is a terminal application.
    desktop_contents.append(read_Y_n("Terminal app? Y/n: "))
    # Ask user if they wish to install an icon.
    install_icon = read_Y_n("Do you wish to install an icon? Y/n: ")
    if install_icon:
        icon_paths = []
        icon_sizes = []
        while True:
            tmp = raw_input("Enter path to icon: ")
            if file_exists(tmp):
                icon_paths.append(tmp)
                if is_global_install():
                    icon_sizes = select_icon_size(icon_sizes)
                # Ask if they wish to install additional icons.
                if not read_Y_n("Install another icon? Y/n: "):
                    break
            else:
                print "Icon not found!"
        desktop_contents.append(icon_paths)
        desktop_contents.append(icon_sizes)
    # Ask user for execution command.
    desktop_contents.append(raw_input("Enter execution command: "))
    return desktop_contents


def desk_installed(program):
    return os.path.isfile(_global_desk_dir + program + ".desktop")


def file_exists(filename):
    return os.path.isfile(filename)


def read_Y_n(prompt):
    while True:
        Y_n = raw_input(prompt)
        if Y_n is "Y" or Y_n is "y":
            return True
        elif Y_n is "N" or Y_n is "n":
            return False
        else:
            print "You need to enter Y or n"

def is_global_install():
    return getpass.getuser() == "root"


def select_icon_size(icon_sizes):
    # Print hicolor/ dirs so user can select icon size.
    (__, dirnames, __) = os.walk("/usr/share/icons/hicolor").next()
    for i in range(len(dirnames)):
        print "[" + str(i) + "] " + str(dirnames[i])
    # Ask user what size icon they are installing.
    while True:
        tmp = int(raw_input("Select icon size 0-" + 
                            str(len(dirnames)-1) + ": "))
        if tmp >= 0 and tmp < len(dirnames):
            icon_sizes.append(dirnames[int(tmp)])
            break
        else:
            print "Invalid selection!"
    return icon_sizes


def generate_dot_desktop():
    print "hello"


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

print is_global_install()

if _args.i:
    print "install"
    install(_args)
elif _args.r:
    print "remove"
elif _args.g:
    print "generate"
else:
    print "Try 'setup.py --help'"
