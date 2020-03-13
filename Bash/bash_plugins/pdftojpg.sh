#!/usr/bin/env bash

pdftojpg(){
  if [[ $# -ne 1 ]]; then
    echo "Usage : pdftojpg FILE"
  else
    local FILE=${1}
    pdftoppm "${FILE}" | ppmtojpeg > "${FILE%.*}.jpg"
  fi
}
