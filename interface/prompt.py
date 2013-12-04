
''' This module contains all functions used to request input from the user.
'''

import utils

def for_string(prompt):
    return raw_input("\n> " + prompt + ": ")

def for_yes_no(prompt):
    while True:
        yes_no = for_string(prompt + " y/n")
        if yes_no in ("y", "Y", "yes", "Yes"):
            return True
        if yes_no in ("n", "N", "no", "No"):
            return False
        print "\nMust enter y or n."

def for_path(prompt):
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
