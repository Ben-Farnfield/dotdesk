import os

'''
Contains all functions used to interface with the user.
'''
def prompt_string(prompt):
    return raw_input(prompt + ": ")

def prompt_Y_n(prompt):
    while True:
        Y_n = raw_input(prompt + "Y/n: ")
        if Y_n is "Y" or Y_n is "y":
            return True
        elif Y_n is "N" or Y_n is "n":
            return False
        else:
            print "You need to enter Y or n"
            
def output_dirs(path):
    (__, dir_names, __) = os.walk(path).next()
    for i in range(len(dir_names)):
        print "[" + str(i) + "] " + str(dir_names[i])  
    return dir_names
