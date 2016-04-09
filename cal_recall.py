#! /urs/bin/env python

"""
argv list:
argv[1]: retrieval sorted result file name
argv[2]: number of points that will be calculate the recall ratio
argv[3]: to show bad case or not(true for show)
argv[4]: number of query images
argv[5]: number of sorted results in one query
"""

import sys
import numpy

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()
    assert(len(lines) == int(sys.argv[4]))
    recall_list = []
    bad_case_num = 0
    for i in xrange(len(lines)):
        results = lines[i].strip().split(';')
        assert(len(results) == int(sys.argv[5]) + 1)
        assert(results[-1] == "")
        hit_num = 0
        for j in xrange(0, int(sys.argv[2])):
            tmp = results[j].strip().split(' ')
            assert(len(tmp) == 2)
            x = int(tmp[1])
            if j == 0:
                if x != i:
                    print x, i
                # assert(x == i)
                assert(float(tmp[0]) < 1e-6)
            if (i / 4 * 4) <= x <= (i / 4 * 4+ 3):
                hit_num = hit_num + 1
        recall_list.append(hit_num)
        if len(sys.argv) > 3:
            if sys.argv[3] == 'true' and hit_num == 1:
            # the Euclidean distance between query image and itself in dataset is 0
                print str(i) + ':',
                for j in xrange(0, int(sys.argv[2])):
                    tmp = results[j].strip().split(' ')
                    print tmp[1],
                print
                bad_case_num = bad_case_num + 1
    if len(sys.argv) > 3 and sys.argv[3] == 'true':
        print 'Bad case (hit number equals 1) number:', bad_case_num
    print numpy.mean(recall_list)

main()
