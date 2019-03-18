#!/bin/bash
DUMP_EXEC=./dump
if [ -f ${DUMP_EXEC} ]; then
    while true; do clear; ${DUMP_EXEC} ; sleep 0.5; done
else
    echo -e "\x1b[1m[\x1b[91mwarn\x1b[0m\x1b[1m]\x1b[0m ${DUMP_EXEC} not found. Try \"make\"."
fi
