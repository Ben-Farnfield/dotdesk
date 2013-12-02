
'''

'''

def option_list(list_to_print):
    for i in range(len(list_to_print)):
        print "{0:>4}.{1:.>12}".format("[" + str(i) + "]", list_to_print[i])
