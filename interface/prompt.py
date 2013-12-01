
'''

'''

from util import this

def for_string(prompt):
    string = raw_input("\n> " + prompt + ": ")
    if string is None:
        return ""
    else:
        return string

def for_yes_no(prompt, error):
    while True:
        yes_no = for_string(prompt + " y/n")
        if yes_no is "Y" or yes_no is "y":
            return True
        elif yes_no is "N" or yes_no is "n":
            return False
        else:
            print "\n" + error

def for_path(prompt, error):
    while True:
        path = for_string(prompt)
        if this.file_exists(path):
            return path
        else:
            print "\n" + error

def to_select(prompt, error, num_options):
    while True:
        select = int(for_string(prompt))
        if select >= 0 and select < num_options:
            return select
        else:
            print "/n" + error
