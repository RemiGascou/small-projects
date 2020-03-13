#!/usr/bin/env bash

pretty_file(){
    if [[ $# == 0 ]]; then $(which file) ; else
        $(which file) ${@} | awk '
        function tree(name, array, arraylen) {
            result = name "\n"
            if (arraylen == 1) { result = result "  └──> " array[1]; }
            else {
                result = result "  ├──> " array[1];
                for (i = 2; i <= arraylen-1; i++) result = result "\n  ├──> " array[i];
                result = result "\n  └──> " array[arraylen];
            }
            return result
        }

        {
            split($0, line, /[:][ ]+/);
            n_elements = split(line[2], elements, ", ");
            print tree(line[1], elements, n_elements);
        }'
    fi
}

alias file="pretty_file"
