
'''

'''

import argparse
import getpass
import sys
import os

# Get arguments passed by user.
def get_args():
    parser = argparse.ArgumentParser(prog="dotdoc")
    parser.add_argument("-i", help="Install .desktop and icon.")
    parser.add_argument("-r", help="Remove .desktop and icon.")
    return parser.parse_args()


# Check if .desktop is already installed.
def make_does_dotdesk_exist(program):
    def does_dotdesk_exist(directory):
        if file_exists(directory + program + ".desktop"):
            view.print_string(program + ".desktop is already installed!")
            sys.exit()

    return does_dotdesk_exist


# Check to see if script run by root user.
def is_root_install():
    return getpass.getuser() == "root"


# Check to see if file is installed.
def file_exists(filename):
    return os.path.isfile(filename)


# Extract file name from end of path.
def extract_file_name_from_path(path):
    split_path = path.split("/")
    return split_path[len(split_path)-1]


# Remove file name from path.
def remove_filename_from_path(path):
    split_path = path.split("/")
    print split_path
    tmp_str = ""
    for i in range(len(split_path)-2): # -2 to cut first " " entry and filename
        tmp_str = tmp_str + "/" + split_path[i+1] # +1 to cut first entry
    return tmp_str + "/"


# Get all directories contained within this folder.    
def get_dirs(path):
    (__, dir_names, __) = os.walk(path).next()
    return dir_names
