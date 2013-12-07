
"""
This module contains all functions used to request input from the user.

for_string()    --  prompts user for string
for_yes_no()    --  prompts user for boolean y/n
for_path()      --  prompts user for path
for_selection() --  prompts user to make a selection
"""

import utils

def for_string(prompt):
    """ Returns a string entered by the user. """
    return raw_input("\n> " + prompt + ": ")

def for_yes_no(prompt):
    """ Returns True for yes and False for no. """
    while True:
        yes_no = for_string(prompt + " y/n")
        if yes_no in ("y", "Y", "yes", "Yes"):
            return True
        if yes_no in ("n", "N", "no", "No"):
            return False
        print "\nMust enter y or n."

def for_path(prompt):
    """
    Returns a string representing the path to a file.

    This function ensures that the file exists and is a valid file
    type for dotdesk before returning a result.
    """
    while True:
        path = for_string(prompt)
        if not utils.file_exists(path):
            print "\nFile not found."
            continue
        if not utils.valid_file_type(path):
            print "\nNot a valid file type."
            continue
        return path

def for_selection(prompt, num_options):
    """ Returns an integer representing the users selection. """
    error = "\nMust select an option between 0 and " + str(num_options-1)
    while True:
        try:
            selection = int(for_string(prompt))
            if selection >= 0 and selection < num_options:
                return selection
            else:
                print error
        except ValueError:
            print error
