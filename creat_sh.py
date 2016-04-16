#! /urs/bin/env python

"""
This script will:
1. Convert caffe out file into characteristics out file of whole image.
The ith line in out file represent characteristics of ith image.
2. Creat .sh file for multiprocess.

argv list:
argv[1]: .out file name
argv[2]: number of images
argv[3]: number of characteristics
argv[4]: characteristics out file name 
argv[5]: key word of lines that in .out file which have output of DNN
argv[6]: number of processes
argv[7]: path of retrieval.py
"""

import node
import sys
import os

def main():
    print_file()
    print "print_file done."
    creat_sh()

def print_file():
    """
    f = open(sys.argv[1])
    lines = [l for l in f.readlines() if 'Batch' in l and (sys.argv[5] + ' = ') in l]
    f.close()
    # we dont need do scan lines in .out file twice
    """
    fin = open(sys.argv[1])
    f = open(sys.argv[4], 'w')
    for i in xrange(0, int(sys.argv[2])):
        for j in xrange(int(sys.argv[3])):
            while True:
                line = fin.readline()
                if 'Batch' in line and (sys.argv[5] + ' = ') in line:
                    break
            assert(('Batch ' + str(i)) in line)
            v = line.strip().split(' = ')[1]
            print >> f, float(v),
        print >> f
    fin.close()
    f.close()

def creat_sh():
    # The method can also be used for modifying .sh file, for instance,
    # increase the number of processes
    f = open('multiprocess.sh', 'w')
    nums_eachprocess = int(sys.argv[2]) / int(sys.argv[6])
    tmp_list = []
    for i in xrange(int(sys.argv[6])):
        tmp_list.append(nums_eachprocess * i)
    tmp_list.append(int(sys.argv[2]))
    py_path = "" if len(sys.argv) < 8 else sys.argv[7]
    tmp_file_list = []
    for i in xrange(int(sys.argv[6])):
        tmp_file_list.append('retrieval_out' + str(i) + '.out')
        print >> f, 'python', py_path + 'retrieval.py', sys.argv[4], tmp_list[i],\
                tmp_list[i+ 1], tmp_file_list[-1], sys.argv[2], '&' 
    f.close()
    fcat = open('cat_rm.sh', 'w')
    print >> fcat, 'cat',
    for tmpf in tmp_file_list:
        print >> fcat, tmpf,
    print >> fcat, '> retrieval.out'
    for tmpf in tmp_file_list:
        print >> fcat, 'rm', tmpf
    fcat.close()

if "__name__" == "__main__":
    main()
