#!/usr/bin/env bash

export TUI_RENDERER=whiptail
export TUI_RENDERER_OPTS='--backtitle "Package configuration"'

load_all_functions(){
    for file in $(find ./functions/ -name "*.sh"); do
        . "${file}"
    done
}

#==============================================================

load_all_functions

exit_to_shell
