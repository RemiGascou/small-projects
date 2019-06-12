#!/usr/bin/env bash

# ============== DirConf Utils ==============
#
#
# dirconf_init    : Creates a .dirconf file
# dirconf_nearest : Loads the nearest .dirconf in parents
# dirconf_cd      : Autoload nearest .dirconf when cd

function dirconf_init () {
    if [[ $1 == '-r' ]]; then
        rm .dirconf
    fi
    if [[ -f ".dirconf" ]]; then
        echo -e "\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m .dirconf already exists."
        echo -e "     | Use \x1b[1mdirconf_init -r\x1b[0m to reset configuration."
    else
        echo "#!/usr/bin/env bash" > .dirconf
        echo "" >> .dirconf
    fi
}

#

function dirconf_nearest() {
    if [[ $# -eq 1 ]]; then
        dir=$1
    else
        dir=$(pwd)
    fi
    FOUND=0
    while [[ $dir != '/' && $dir != '.' && $dir != './' ]]; do
        if [[ -f "$dir/.dirconf" ]]; then
            source "$dir/.dirconf"
            FOUND=1
            break;
        fi
        dir="$(dirname "$dir")"
    done
    if [[ ${FOUND} -eq 0 ]]; then
        source ~/.bashrc
    fi
}

#

function dirconf_cd() {
    cd "$@"
    dirconf_nearest
}

alias cd="dirconf_cd"
