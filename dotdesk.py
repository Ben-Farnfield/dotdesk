#! /usr/bin/python

import argparse
import getpass
import shutil
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
    

def is_installed(desktop):
    return os.path.isfile()

def install():
    print "test"

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

args = get_args()

if args.i:
    print "install"
    
elif args.r:
    print "remove"
elif args.g:
    print "generate"
else:
    print "Try 'setup.py --help'"
