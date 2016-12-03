#! /usr/bin/env python

"""
This file is used to creat training and testing pic pairs of UKBench dataset for image retrieval.

argv list:
argv[1 - 4]: train, test, train_p, test_p files names
argv[5]: number of negative pairs of each image
"""

import sys
image_path = 'jpg_3232'
import os
images = os.listdir(image_path)
images = sorted(images)
import sys, random
assert(len(images) == 10200)
import node
pair_list = []
for i in xrange(0, 10200, 4):
    for j in xrange(4):
        for k in xrange(4):
            pair_list.append(node.Pair_Record(i + j, i + k, 1))
        for k in xrange(int(sys.argv[5])):
            x = random.randint(0, 10199)
            while (i <= x <= i + 3):
                x = random.randint(0, 10199)
            pair_list.append(node.Pair_Record(i + j, x, 0))
assert(len(pair_list) == 10200 * (4 + int(sys.argv[5])))
random.shuffle(pair_list)
train_file = open(sys.argv[1], 'w')
test_file = open(sys.argv[2], 'w')
train_file_p = open(sys.argv[3], 'w')
test_file_p = open(sys.argv[4], 'w')
for i in xrange(0, len(pair_list) / 10 * 9):
    print >> train_file, image_path + os.sep + images[pair_list[i].left_index], pair_list[i].v
    print >> train_file_p, image_path + os.sep + images[pair_list[i].right_index], pair_list[i].v
for i in xrange(len(pair_list) / 10 * 9, len(pair_list)):
    print >> test_file, image_path + os.sep + images[pair_list[i].left_index], pair_list[i].v
    print >> test_file_p, image_path + os.sep + images[pair_list[i].right_index], pair_list[i].v
train_file.close()
test_file.close()
train_file_p.close()
test_file_p.close()
