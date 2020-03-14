#!/usr/bin/env bash

exit_to_shell(){
    local SHELL="/bin/bash"

    rows=$(stty size | cut -d' ' -f1)
    [ -z "$rows" ] && rows=$high
    [ $rows -gt $high ] && rows=$high
    cols=$(stty size | cut -d' ' -f2)

    ${TUI_RENDERER} ${TUI_RENDERER_OPTS} \
        --title "Exit to shell" \
        $OPTS \
        --yesno '' $rows $((cols - 5))

    echo ""
    echo " To go back to the TUI, type : "
    echo ""
    cd /; ${SHELL}
}
