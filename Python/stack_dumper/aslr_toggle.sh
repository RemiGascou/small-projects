#!/usr/bin/env bash

log()  { echo -e "\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m ${@}";  }
info() { echo -e "\x1b[1m[\x1b[92mINFO\x1b[0m\x1b[1m]\x1b[0m ${@}"; }
warn() { echo -e "\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m ${@}"; }

aslr_get_state() {
    local STATE=$(cat /proc/sys/kernel/randomize_va_space)
    echo ${STATE}
}

aslr_set_state() {
    local NEWSTATE="${1}"
    echo ${NEWSTATE} > /proc/sys/kernel/randomize_va_space
}

#===============================================================================

if [ "$EUID" -ne 0 ]; then
    warn "You need to be root to change ASLR parameters."
    exit
else
    CURRENT_STATE=$(aslr_get_state)
    if [[ ${CURRENT_STATE} != 0 ]]; then
        log "ASLR was \x1b[92menabled\x1b[0m (value ${CURRENT_STATE}), disabling it..."
        aslr_set_state 0
        info "Done."
    else
        log "ASLR was \x1b[91mdisabled\x1b[0m (value ${CURRENT_STATE}), enabling it..."
        aslr_set_state 2
        info "Done."
    fi
fi
