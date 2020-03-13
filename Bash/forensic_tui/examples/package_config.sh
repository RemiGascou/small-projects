#!/usr/bin/env bash

output=$(dialog --backtitle "Package configuration" \
                --title "Configuration sun-java-jre" \
                --menu "$(parted -l)" 15 40 4 1 "sda1" 2 "sda2" 3 "sda3" \
         3>&1 1>&2 2>&3 3>&-
)
clear; echo "Choice was : $output"
