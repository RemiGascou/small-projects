#!/bin/bash

log()  { echo -e "\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m ${@}";  }
info() { echo -e "\x1b[1m[\x1b[92mINFO\x1b[0m\x1b[1m]\x1b[0m ${@}"; }
warn() { echo -e "\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m ${@}"; }

gen_full_testfile(){
    local FILE=${1}
    printf ""         >  ${FILE}    # Creates File
    printf "  "       >> ${FILE}    # push
    printf " \n "     >> ${FILE}    # dup
    printf " \n\t"    >> ${FILE}    # swap
    printf " \n\n"    >> ${FILE}    # pop
    printf "\t   "    >> ${FILE}    # add
    printf "\t  \t"   >> ${FILE}    # sub
    printf "\t  \n"   >> ${FILE}    # mul
    printf "\t \t "   >> ${FILE}    # div
    printf "\t \t\t"  >> ${FILE}    # mod
    printf "\t\t "    >> ${FILE}    # store
    printf "\t\t\t"   >> ${FILE}    # load
    printf "\n   \t\t  \n"     >> ${FILE} # lbl  100 (TSS)
    printf "\n \t \t\t  \n"    >> ${FILE} # call 100
    printf "\n \n \t\t  \n"    >> ${FILE} # jmp  100
    printf "\n\t  \t\t  \n"    >> ${FILE} # jmpz 100
    printf "\n\t\t \t\t  \n"   >> ${FILE} # jmpn 100
    printf "\n\t\n"   >> ${FILE}    # leave
    printf "\n\n\n"   >> ${FILE}    # end
    printf "\t\n  "   >> ${FILE}    # printc
    printf "\t\n \t"  >> ${FILE}    # printn
    printf "\t\n\t "  >> ${FILE}    # readc
    printf "\t\n\t\t" >> ${FILE}    # readn
}

#====================================================

gen_full_testfile "../testprograms/full.ws"

for file in $(find ../testprograms -name "*.ws"); do
    log "Testing ${file}"
    ./bin/decompiler < "${file}"

done
