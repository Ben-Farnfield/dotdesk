
'''

'''

from util import util
from util import const

def prompt_string(prompt):
    return raw_input(prompt + ": ")


def prompt_Y_n(prompt):
    while True:
        Y_n = raw_input(prompt + " Y/n: ")
        if Y_n is "Y" or Y_n is "y":
            return True
        elif Y_n is "N" or Y_n is "n":
            return False
        else:
            print "You need to enter Y or n"


def prompt_path(prompt, error):
    while True:
        path = prompt_string(prompt)
        if util.file_exists(path):
            return path
        else:
            print error


def prompt_select(prompt, error, num_options):
    while True:
        select = int(prompt_string(prompt))
        if select >= 0 and select < num_options:
            return select
        else:
            print error


def print_list(list_to_print):
    for i in range(len(list_to_print)):
        if i < 10:
            select = " [" + str(i) + "] " # extra space so options line up
        else:
            select = "[" + str(i) + "] "
            
        print select + str(list_to_print[i])


def print_header(action, name):
    print const.DOTDESK_HEADER.format(action=action, name=name)
