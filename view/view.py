
'''

'''


from util import util


__author__ = "Ben Farnfield"
__email__ = "ben.farnfield@gmail.com"

__license__ = ""


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
            
def print_dirs(path):
    dir_names = util.get_dirs(path)
    for i in range(len(dir_names)):
        print "[" + str(i) + "] " + str(dir_names[i])
