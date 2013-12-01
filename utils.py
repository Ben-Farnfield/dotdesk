
'''

'''

import argparse
import getpass
import os

    # ---------------------------- session ---------------------------- #

def get_args():
    ''' Returns the parsed arguments passed by the user '''
    parser = argparse.ArgumentParser(prog="dotdesk")
    parser.add_argument("-i", help="Install .desktop and icon")
    parser.add_argument("-r", help="Remove .desktop and icon")
    return parser.parse_args()

def is_NOT_root_user():
    return getpass.getuser() != "root"

    # ------------------------------ file ----------------------------- #

def exists(path):
    return os.path.isfile(path)

def type(path): 
    file_type 

def copy(loc, dst):
    ''' Copies file from location to destination '''
    # Need to deal with exceptions.
    pass
