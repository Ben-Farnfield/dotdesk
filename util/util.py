
'''

'''


import argparse
import getpass
import sys
import os


__author__ = "Ben Farnfield"
__email__ = "ben.farnfield@gmail.com"

__license__ = ""


# Get arguments passed by user.
def get_args():
    parser = argparse.ArgumentParser(prog="dotdoc")
    parser.add_argument("-i", help="Install .desktop and icons.")
    #~ parser.add_argument("-r", action="store_true",
                        #~ help="Remove .desktop and icons")
    return parser.parse_args()

# Check if .desktop is already installed.
def make_does_dotdesk_exist(program):
	def does_dotdesk_exist(directory):
		if file_exists(directory + program + ".desktop"):
			print program + ".desktop is already installed!"
			sys.exit()

	return does_dotdesk_exist

# Check to see if script run by root user.
def is_root_install():
    return getpass.getuser() == "root"

# Check to see if file is installed.
def file_exists(filename):
    return os.path.isfile(filename)

# Extract file name form end of path.
def extract_file_name_from_path(path):
	split_path = path.split("/")
	return split_path[len(split_path)-1]
			
# Get all directories contained within this folder.    
def get_dirs(path):
	(__, dir_names, __) = os.walk(path).next()
	return dir_names
