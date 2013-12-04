#! /usr/bin/python

'''
This script is used to install and remove dotdesk.

Author: Ben Farnfield
Contact: ben.farnfield@gmail.com
'''

import utils

import os
import sys
import stat

SCRIPT = "/usr/bin/dotdesk"

    # ---------------------------- help --------------------------- #

HELP_INFO = ("\n{:<20}{:>20}".format("To install dotdesk:",
                                     "sudo ./install.py -i") + 
             "\n{:<20}{:>20}\n".format("To remove dotdesk:",
                                       "sudo ./install.py -r"))

HELP_TIP = "Try: 'sudo ./install.py -h' for more info."

    # ------------------------- check user ------------------------- #

if utils.is_NOT_root_user():
    print HELP_INFO
    sys.exit()

    # ----------------------- install dotdesk ---------------------- #

def install():
    cwd = os.getcwd()
    script_contents = ("#! /bin/bash\n" +
                       " " +
                       cwd + "/main.py \"$@\"")

    utils.write_file(SCRIPT, script_contents,
                     "\ndotdesk installed!\n",
                     "\n!!Issue installing dotdesk!!\n")
    try:
        st = os.stat(SCRIPT)
        os.chmod(SCRIPT, st.st_mode |
                 stat.S_IXUSR |
                 stat.S_IXGRP |
                 stat.S_IXOTH)
    except OSError as e:
        print str(e)
        print "Issue setting permissions for " + SCRIPT
        sys.exit()

    # ----------------------- remove dotdesk ----------------------- #

def remove():
    utils.remove_file(SCRIPT,
                      "\ndotdesk removed!\n",
                      "\n!!Issue removing dotdesk!!")

    # ------------------------- parse args ------------------------- #

args = sys.argv
len_args = len(args)

if len_args == 2:
    flag = args[1]
else:
    print HELP_TIP

if flag in ("-i", "--install"):
    install()
elif flag in ("-r", "--remove"):
    remove()
elif flag in ("-h", "--help"):
    print HELP_INFO
else:
    print HELP_TIP
