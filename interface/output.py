
"""
This module provides functions which output information to the user.

option_list()   --  prints a list as a menu
line()          --  prints a 30 char dashed line
"""

def option_list(prompt, list_to_print):
    """ Prints a numbered list to stdout. """
    print "\n" + prompt + ":\n"
    for i in range(len(list_to_print)):
        print "{0:>4}.{1:.>12}".format("[" + str(i) + "]", list_to_print[i])

def line():
    """ Prints a 30 char dashed line to stdout. """
    print "\n{:-<30}\n".format("")
