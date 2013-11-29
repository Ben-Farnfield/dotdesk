#! /usr/bin/python

'''

'''

from control.install import install
from control.remove import remove
from util import util
from view import view

args = util.get_args()

# output supported icon formats.

# adv if run in root or not and what that means.

if args.i:
    install(args)
elif args.r:
    remove(args)
else:
    view.print_string("Try 'setup.py --help'")
