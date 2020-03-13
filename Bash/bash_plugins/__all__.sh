#!/usr/bin/env bash

SAVEIFS=${IFS}
IFS=$(echo -en "\n\b")

for plugin_file in ~/.bash_plugins/* ; do
    if [[ $(basename ${plugin_file}) != "__all__.sh" ]]; then
        . "${plugin_file}";
    fi;
done

IFS=${SAVEIFS}
