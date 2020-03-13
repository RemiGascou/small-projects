#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage : ./beautify.sh file"
else
    NCOLOR="\x1b[1;91m"
    SCOLOR="\x1b[1;93m"
    TCOLOR="\x1b[1;96m"
    cat ${1} \
    | sed "s/\t/${TCOLOR}T\x1b[0m/g"   \
    | sed "s/ /${SCOLOR}S\x1b[0m/g"    \
    | sed ":a;N;\$!ba;s/\n/${NCOLOR}N\x1b[0m\n/g"
    echo ""
fi
