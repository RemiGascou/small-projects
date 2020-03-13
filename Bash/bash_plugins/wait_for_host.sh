#!/usr/bin/env bash

wait_for_host(){
    local HOST="${1}"
    echo -e "\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m Waiting for ${HOST} to be up ..."
    local WAITING=1
    while [[ ${WAITING} == 1 ]]; do
        local RESULT=$(ping -c 1 -w 1 "${HOST}")
        if [[ $(echo "${RESULT}" | grep "0% packet loss" | wc -l) != 0 ]]; then local WAITING=0; fi
        sleep 0.5
    done
    echo -e "\x1b[1m[\x1b[92mINFO\x1b[0m\x1b[1m]\x1b[0m ${HOST} is up !"
}
