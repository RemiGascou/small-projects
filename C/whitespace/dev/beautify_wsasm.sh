#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage : ./beautify.sh file"
else
    COLOR_KEYWORD="\x1b[1m\x1b[95m"
    COLOR_LABEL="\x1b[1m\x1b[94m"
    COLOR_COMMENT="\x1b[1m\x1b[96m"
    cat ${1} \
    | sed -e "s/\(push\|dup\|swap\|pop\|add\|sub\|mul\|div\|mod\|store\|load\|lbl\|call\|jmp\|jmpz\|jmpn\|leave\|end\|printc\|printn\|readc\|readn\)/${COLOR_KEYWORD}\1\x1b[0m/g" \
    | sed -e "s/\(;.*\)/${COLOR_COMMENT}\1\x1b[0m/g"
    echo ""
fi

# |push|dup|swap|pop|add|sub|mul|div|mod|store|load|lbl|call|jmp|jmpz|jmpn|leave|end|printc|printn|readc|readn
