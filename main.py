#! /usr/bin/python

'''

'''

import utils
from control.install import install

import sys

# Get command line args before checking user privileges so the -h command can
# be run by any user.
args = utils.get_args()

if utils.is_NOT_root_user():
    print "You do not have the correct privileges. Please run as 'root' user."
    sys.exit()

if args.i:
    install(args)
elif args.r:
    pass
else:
    print "Try 'dotdesk -h'"
