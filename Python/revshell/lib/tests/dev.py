#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import pexpect
import time, datetime

def readfile(file, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "r"+b_opt)
    data = f.readlines()
    f.close()
    return data

def writefile(file, data, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "w"+b_opt)
    for e in data:
        f.write(e)
    f.close()
    return data

def get_numbers():
    lines = ""
    child = pexpect.spawn("nc ctfchallenges.ritsec.club 8001")
    child.expect('Are you starting')
    date_1 = str(datetime.datetime.now().time())
    date_2 = str(time.mktime(datetime.datetime.now().timetuple()))
    lines += child.before.decode("UTF-8")
    child.expect('Can you guess')
    lines += child.before.decode("UTF-8")
    numbers = []
    for line in lines.split("\n"):
        if 'pattern' not in line and line != "":
            numbers.append(int(line))
    return [date_1, date_2, ""]+[str(c) for c in numbers]
    # return numbers

nb_tests = 1001
data = ["Time", "Unix time", "Number 1", "Number 2", "Number 3", "Number 4", "Number 5"]
for k in range(1, nb_tests+1):
    print("\r\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m Currently getting numbers for test %4d" % k, end='')
    data.append(';'.join(get_numbers())+"\n")
print("")

writefile("out_"+str(nb_tests)+".csv",data)
