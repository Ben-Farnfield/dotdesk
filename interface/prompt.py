
'''

'''

import utils

def for_string(prompt):
    string = raw_input("\n> " + prompt + ": ")
    if string is None:
        return ""
    return string

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
        icon_type = utils.file_type(path)
        if not utils.valid_file_type(icon_type):
            print "\nNot a valid file type."
            continue
        return path

def for_selection(prompt, num_options):
    while True:
        select = int(for_string(prompt))
        if select >= 0 and select < num_options:
            return select
        print "/nMust select an option between 0 and " + str(num_options-1)
