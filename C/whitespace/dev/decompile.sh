#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage : ./decompile.sh file"
else
    ./bin/decompiler < $1
fi
