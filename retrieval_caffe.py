#! /urs/bin/env python

"""
This file will calculate distance between every two vectors of images and sort the distances.
Using for retrival in caffe network output file.

argv list:
argv[1]: .out file name
argv[2]: number of images
argv[3]: number of characteristics
argv[4]: number of results after sorted that will be showed
argv[5]: key word of lines that in .out file which have output of DNN

Every line in .out file represent retrieval list of one image after sorted.
Line 0 represents retrieval result of image 0, line 1 represents image 2.
Print format of each line:
distance image_index_of_this_distance
"""

import node
import os
import sys

def main():
    f = open(sys.argv[1])
    lines = [l for l in f.readlines() if 'Batch' in l and (sys.argv[5] + ' = ') in l]
    f.close()
    # assert(len(lines) == int(sys.argv[2]) * int (sys.argv[3]))
    line_no = 0
    node_list = []
    for i in xrange(0, int(sys.argv[2])):
        record_list = []
        for j in xrange(int(sys.argv[3])):
            assert(('Batch ' + str(i)) in lines[line_no])
            v = lines[line_no].strip().split(' = ')[1]
            record_list.append(node.Record(j, float(v)))
            line_no = line_no + 1
        node_list.append(node.Node(record_list))
    del lines
    retrieval(node_list)

def retrieval(node_list):
    recall_list = []
    for i in xrange(0, len(node_list)):
        retrieval_list = []
        for j in xrange(0, len(node_list)):
            dis = node_list[i].cal_dis(node_list[j])
            retrieval_list.append(node.Record(j, dis))
        retrieval_list = sorted(retrieval_list, key = lambda x : x.v)
        print_evaluate(i, retrieval_list)
        # cal_recall(i, retrieval_list, recall_list)

def print_evaluate(i, retrieval_list):
    for j in xrange(int(sys.argv[4])):
        print retrieval_list[j].v, str(retrieval_list[j].index) + ';',
    print

def cal_recall(i, retrieval_list, recall_list):
    hit_num = 0
    assert(retrieval_list[0].index == i)
    for j in xrange(int(sys.argv[4])):
        if (i / 4 * 4) <= retrieval_list[j].index <= (i / 4 * 4+ 3):
            hit_num = hit_num + 1
    recall_list.append(hit_num)

if "__name__" == "__main__":
    main()
