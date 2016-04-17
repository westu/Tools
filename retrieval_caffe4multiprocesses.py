#! /urs/bin/env python

"""
argv list:
argv[1]: input file name
argv[2], argv[3]: retrieval job of image [argv[2], argv[3])
argv[4]: output file name
argv[5]: number of images
"""

import sys
import node

def main():
    fout = open(sys.argv[4], 'w')
    for i in xrange(int(sys.argv[2]), int(sys.argv[3])):
        """
        f = open(sys.argv[1])
        for j in xrange(0, i):
            f.readline()
        cha_list = get_cha_list(f.readline())  # characteristic list
        # assert(len(cha_list) == 4096)  # for testing
        this_node = node.Node(cha_list)
        f.close()
        f = open(sys.argv[1])
        dis_list = []
        total_image_num = 10200 if len(sys.argv) < 6 else int(sys.argv[5])
        for j in xrange(0, total_image_num):
            tmp_node = node.Node(get_cha_list(f.readline())) 
            dis_list.append(node.Record(j, this_node.cal_dis(tmp_node))) 
        f.close()
        # The codes above will save memory when running, but it will read file
        # from disk for many times, it may make it run slowly.
        """
        f = open(sys.argv[1])
        lines = f.readlines()
        f.close()
        cha_list = get_cha_list(lines[i])  # characteristic list
        # assert(len(cha_list) == 4096)  # for testing
        this_node = node.Node(cha_list)
        dis_list = []
        total_image_num = 10200 if len(sys.argv) < 6 else int(sys.argv[5])
        for j in xrange(0, total_image_num):
            tmp_node = node.Node(get_cha_list(lines[j])) 
            dis_list.append(node.Record(j, this_node.cal_dis(tmp_node))) 
        dis_list = sorted(dis_list, key = lambda x : x.v)
        for dis in dis_list:
            print >> fout, dis.v, str(dis.index) + ';',
        print >> fout
    fout.close()

def get_cha_list(line):
    line = line.strip().split(' ')
    if line[-1] == '':
        del line[-1]
    return [node.Record(i, float(line[i])) for i in xrange(0, len(line))]

if "__name__" == "__main__":
    main()
