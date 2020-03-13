#!/usr/bin/env bash

log()  { echo -e "\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m ${@}";  }
info() { echo -e "\x1b[1m[\x1b[92mINFO\x1b[0m\x1b[1m]\x1b[0m ${@}"; }
warn() { echo -e "\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m ${@}"; }



if [[ $# -ne 1 ]]; then
    echo "Usage : ${0} WORDLIST"
else
    WORDLIST="${1}"
    TITLE="TLS-SEC"
    EXCLAMATION="BULLSHIT!!"
    TERMS=$(cat ${WORDLIST} | sed ':a;N;$!ba;s/\n/%0D%0A/g' )
    LINK="https://www.bullshitbingo.net/cards/custom/?title=${TITLE}&exclamation=${EXCLAMATION}&free_square=&terms=${TERMS}"

    firefox "${LINK}" &
fi
