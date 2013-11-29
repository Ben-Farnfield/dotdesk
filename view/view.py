
'''

'''

from util import util
from util import const

def prompt_string(prompt):
    string = raw_input("\n> " + prompt + ": ")
    if string is None:
        return ""
    else:
        return string 


def prompt_Y_n(prompt):
    while True:
        Y_n = prompt_string(prompt + " Y/n")
        if Y_n is "Y" or Y_n is "y":
            return True
        elif Y_n is "N" or Y_n is "n":
            return False
        else:
            print_string("\nYou need to enter Y or n")


def prompt_path(prompt, error):
    while True:
        path = prompt_string(prompt)
        if util.file_exists(path):
            return path
        else:
            print_string(error)


def prompt_select(prompt, error, num_options):
    while True:
        select = int(prompt_string(prompt))
        if select >= 0 and select < num_options:
            return select
        else:
            print_string(error)


def print_string(string):
    print string


def print_list(list_to_print):
    for i in range(len(list_to_print)):
        if i < 10:
            select = " [" + str(i) + "] " # extra space so options line up
        else:
            select = "[" + str(i) + "] "
            
        print_string(select + str(list_to_print[i]))
