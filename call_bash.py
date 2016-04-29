#!/usr/bin/python3

import sys
import os
from subprocess import Popen, PIPE
from functools import reduce


def file_printer(num):
    bash_cmd = "./bash_exe.sh %s" % num
    p = Popen(bash_cmd.split(), stdout=PIPE, stderr=PIPE)
    output,error = p.communicate()

    out_str = output.strip()
    strip_std_out = out_str.split()

    str_list =[]
    count = 0
    for i in strip_std_out:
        str_list.append(i.decode('UTF-8')) 
        count += 1
    for i in str_list:
        if i not in ["1","2","3","4","5"]:
            print(i, str_list[count-1])



    if error:
        print("This is the error! %s " % error) 



if __name__ == "__main__":

    file_printer(sys.argv[1])
