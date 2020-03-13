#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage : ./compile.sh file"
else
    ./compiler/compiler < $1
fi
