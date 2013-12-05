#! /usr/bin/python

''' dotdesk is a simple Python utility written to create and install .desktop
    files along with their companion icons.

    This module provides argument parsing for dotdesk.

    Author: Ben Farnfield
    Contact: ben.farnfield@gmail.com
'''

import utils
from action.install import install
from action.remove import remove

import sys

HELP_INFO = ("\n" +
             "Usage: dotdesk [OPTION] [PROGRAM NAME]\n" +
             "\n" +
             "dotdesk is a simple utility written to create and install " +
             ".desktop files along with their companion icons.\n" +
             "\n" +
             "Arguments:\n" +
             "{:>5}{:>10}        {:<}\n".format("-i,", "--install",
                                                "install a .desktop file.") + 
             "{:>5}{:>10}        {:<}\n".format("-r,", "--remove",
                                                "remove a .desktop file."))

def main():

    if utils.is_NOT_root_user():
        print ("You don't have the correct privileges to run dotdesk. " +
               "Please run as 'root' user.")
        sys.exit()

    args = utils.get_args()
    
    if args["flag"] in ("-i", "--install"):
        install(args)
    elif args["flag"] in ("-r", "--remove"):
        remove(args)
    elif args["flag"] in ("-h", "--help"):
        print HELP_INFO
    else:
        print "Try: 'dotdesk -h' for more info."
        sys.exit()

try:
    main()
except KeyboardInterrupt:
    print "\n"
