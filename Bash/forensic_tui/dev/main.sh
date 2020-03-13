#!/usr/bin/env bash

export TUI_RENDERER=whiptail

load_all_functions(){
    for file in $(find ./functions/ -name "*.sh"); do
        . "${file}"
    done
}

#==============================================================

load_all_functions

exit_to_shell
