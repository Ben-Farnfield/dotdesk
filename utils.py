
'''

'''

import const

import argparse
import getpass
import shutil
import os

    # ---------------------------- session ---------------------------- #

def get_args():
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

def valid_file_type(path):
    f_type = file_type(path)
    for valid_type in const.ICON_TYPES:
        if f_type == valid_type:
            return True
    return False

def copy_file(src, dst):
    try:
        shutil.copy_file(src, dst)
        return True
    except (IOError, Error) as e:
        print str(e)
        return False

def write_file(path, contents):
    try:
        doc = open(path, "w")
        doc.write(contents)
        return True
    except IOError as e:
        print str(e)
        return False
    finally:
        doc.close()
