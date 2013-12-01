
'''

'''

def this_list(list_to_print):
    for i in range(len(list_to_print)):
        if i < 10:
            # one extra space at start so all options line up.
            select = " [" + str(i) + "] "
        else:
            select = "[" + str(i) + "] "
            
        print select + str(list_to_print[i])
