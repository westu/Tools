#! /usr/bin/env python

"""
This file will provide some class for retrieval or something else.
"""

class Node(object):
    def __init__(self, v_list):
        self.v_list = v_list
    def cal_dis(self, node2):
        assert(len(self.v_list) == len(node2.v_list))
        dis = 0
        for i in xrange(0, len(self.v_list)):
            dis = dis + (self.v_list[i].v  - node2.v_list[i].v) ** 2
        import math
        return math.sqrt(dis)

class Record(object):    
    def __init__(self, index, v):
        self.index = index
        self.v = v

class Pair_Record(object):
    def __init__(self, left_index, right_index, v):
        self.left_index = left_index
        self.right_index = right_index
        self.v = v
