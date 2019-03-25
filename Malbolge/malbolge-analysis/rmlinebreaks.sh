#!/bin/bash

echo `sed ':a;N;$!ba;s/\n//g' $1` > $1
