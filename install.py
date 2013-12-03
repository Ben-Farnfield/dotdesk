#! /usr/bin/python

'''

'''

import utils

import os
import sys
import stat

_script = "/usr/bin/dotdesk"
_help_msg = ("\n{:<20}{:>20}".format("To install dotdesk:",
                                     "sudo ./install.py -i") + 
             "\n{:<20}{:>20}\n".format("To remove dotdesk:",
                                       "sudo ./install.py -r"))

if utils.is_NOT_root_user():
    print _help_msg
    sys.exit()


def install():
    cwd = os.getcwd()
    script_contents = ("#! /bin/bash\n" +
                       " " +
                       cwd + "/main.py $1 $2")

    utils.write_file(_script, script_contents,
                     "\ndotdesk installed!\n",
                     "\n!!Issue installing dotdesk!!\n")
    try:
        st = os.stat(_script)
        os.chmod(_script, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    except OSError as e:
        print str(e)
        print "Issue setting permissions for " + _script
        sys.exit()


def remove():
    utils.remove_file(_script,
                      "\ndotdesk removed!\n",
                      "\n!!Issue removing dotdesk!!")


if len(sys.argv) == 2:
    __, arg1 = sys.argv
    if arg1 == "-i":
        install()
    elif arg1 == "-r":
        remove()
    else:
        print _help_msg
else:
    print _help_msg
