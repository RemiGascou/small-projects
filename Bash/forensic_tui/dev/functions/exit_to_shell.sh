#!/usr/bin/env bash

exit_to_shell(){
    local SHELL="/bin/bash"
    echo ""
    echo " To go back to the TUI, type : "
    echo ""
    cd /; ${SHELL}
}
