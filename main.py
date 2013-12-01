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
    print "install"
    install(args)
elif args.r:
    print "remove"
else:
    print "Try 'dotdesk -h'"
