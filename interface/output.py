
'''

'''

def option_list(prompt, list_to_print):
    print "\n" + prompt + ":\n"
    for i in range(len(list_to_print)):
        print "{0:>4}.{1:.>12}".format("[" + str(i) + "]", list_to_print[i])

def line():
    print "\n{:-<30}\n".format("")
