#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage : ./compile.sh file"
else
    ./bin/compiler < $1
fi
