
'''
This class provides all the general utilities required by dotdesk.
'''

import const

import argparse
import getpass
import shutil
import os
import sys

    # ---------------------------- session ---------------------------- #

def get_args():
    ''' Returns a dictionary containing the option set by the user as well
        as the program name. You can access these using "flag" and "name".
    '''
    args = sys.argv
    len_args = len(args)
    
    if len_args == 0:
        print "Try: 'dotdesk -h' for more info."
        sys.exit()
    if len_args > 1:
        flag = args[1]
        name = ""
    if len_args > 2:
        name = args_to_name(args[2:])

    return {"flag":flag, "name":name}

def is_NOT_root_user():
    return getpass.getuser() != "root"

def args_to_name(args_list):
    ''' Concatenates the provided arg list into a space separated name. '''
    name = "".join(arg + " " for arg in args_list)
    return name.rstrip()

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

def copy_file(src, dst, msg=None, error=None):
    try:
        shutil.copyfile(src, dst)
        if msg is not None:
            print msg
    except IOError as e:
        print str(e)
        if error is not None:
            print error
        sys.exit()

def write_file(path, contents, msg=None, error=None):
    try:
        doc = open(path, "w")
        doc.write(contents)
        if msg is not None:
            print msg
    except IOError as e:
        print str(e)
        if error is not None:
            print error
        sys.exit()
    finally:
        doc.close()

def remove_file(path, msg=None, error=None):
    try:
        os.remove(path)
        if msg is not None:
            print msg
    except OSError as e:
        print str(e)
        if error is not None:
            print error
        sys.exit()
