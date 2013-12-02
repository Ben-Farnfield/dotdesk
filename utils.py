
'''

'''

import const

import argparse
import getpass
import shutil
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

def file_exists(path):
    return os.path.isfile(path)

def file_type(path):
    try:
        start = path.rindex(".")
        return path[start:len(path)]
    except ValueError as e:
        print "\nNo file type found!"
        return ""

def valid_file_type(file_type):
    for valid_type in const.ICON_TYPES:
        if file_type is valid_type:
            return True

    return False

def copy_file(src, dst):
    try:
        shutil.copy_file(src, dst)
        return True
    except (IOError, Error) as e:
        print str(e)
        return False
