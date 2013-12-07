
"""
This module provides all the general functions required by dotdesk.

get_args()          -- return command line args
is_NOT_root_user()  -- return True if not root user
file_exists()       -- return True if file exists
file_type()         -- return file extension e.g. '.png'
valid_file_type()   -- return True if file type supported by dotdesk
proc_file()         -- copy, write and remove files
"""

import const

import argparse
import getpass
import shutil
import os
import sys

    # ---------------------------- session ---------------------------- #

def get_args():
    """
    Returns any command line arguments passed by the user.
    
    This function returns a dictionary containing the flag and program name
    passed by the user. You can access the flag using the 'flag' key and
    program name using the 'name' key.
    """
    args = sys.argv
    len_args = len(args)
    
    if len_args == 0:
        print "Try: 'dotdesk -h' for more info."
        sys.exit()
    if len_args > 1:
        flag = args[1]
        name = ""
    if len_args > 2:
        name = _args_to_name(args[2:])

    return {"flag":flag, "name":name}

def _args_to_name(args_list):
    """ Returns the lists contents as a space separated string. """
    name = "".join(arg + " " for arg in args_list)
    return name.rstrip()

def is_NOT_root_user():
    """ Returns True if user is not root. """
    return getpass.getuser() != "root"

    # ------------------------------ file ----------------------------- #

def file_exists(path):
    """ Returns True if this file exists. """
    return os.path.isfile(path)

def file_type(path):
    """ Returns this files extension e.g. '.png' """
    try:
        start = path.rindex(".")
        return path[start:len(path)]
    except ValueError as e:
        print "\nNo file type found!"
        return ""

def valid_file_type(path):
    """ Returns True if this file type is supported by dotdesk. """
    f_type = file_type(path)
    for valid_type in const.ICON_TYPES:
        if f_type == valid_type:
            return True
    return False

def proc_file(proc, path, arg=None, msg=None, error=None):
    """
    Write, copy and remove files.

    This function provides all the file processing functionality required by 
    dotdesk. 
    If an error is raised within this function it will exit the 
    program; a failure here means the script cannot complete its primary
    functions of installation and removal.

    Keyword arguments:
    proc   -- string "w" or "write", "c" or "copy", "r" or "remove"
    path   -- string representing the path to the file to be processed
    arg    -- use changes based on action:
                - "c" or "copy"; string representing destination path
                - "w" or "write"; string representing content to be written
    msg    -- printed if action is successfully completed (default no msg)
    error  -- printed if action fails (default no msg)
    """
    try:
        if proc in ("c", "copy"):
            shutil.copyfile(path, arg)
        elif proc in ("w", "write"):
            with open(path, "w") as doc:
                doc.write(arg)
        elif proc in ("r", "remove"):
            os.remove(path)
        else:
            raise Exception("Invalid arg passed to action")
        if msg is not None:
            print msg
    except Exception as e:
        if error is not None:
            print str(e)
            print error
        sys.exit()
