#! /bin/bash

################################
# This script installs dotdesk #
################################

DIR=$(pwd)

if [ "$1" = "-i" ]; then
    if [ -f /usr/bin/dotdesk ]; then
        printf "dotdesk is already installed\n"
    else
        sudo ln -s $DIR/main.py /usr/bin/dotdesk
        printf "dotdesk has been installed\n"
    fi
elif [ "$1" = "-r" ]; then
    if [ -f /usr/bin/dotdesk ]; then
        sudo rm /usr/bin/dotdesk
        printf "dotdesk has been removed\n"
    else
        printf "dotdesk is not installed\n"
    fi
else
    printf "Try: 'sh install.sh [-i OR -r]'\n"
fi
