#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
from collections import defaultdict
"""
    python 实现计数排序
"""
def counting_sort(a_list, key=lambda x: x):
    """
        计数排序：
        在数的范围很小时还是不错的，当数的范围很大的时候就不适用了，计数排序一般用于基数排序中
    """
    b_list, c_list = [], defaultdict(list)  # Output and "counts"
    for x in a_list:
        c_list[key(x)].append(x)  # "Count" key(x)

    for k in range(min(c_list), max(c_list) + 1):  # For every key in the range
        b_list.extend(c_list[k])  # Add values in sorted order
    return b_list


if __name__ == '__main__':
    lst = random.sample(xrange(100), 10)
    # lst = [randrange(100) for i in range(10)]
    alist = lst[:]

    print '-'*50
    print u'待排序序列为：%s' %(lst) 
    seq = counting_sort(alist)

    print u'计数排序后序列为：%s' %seq

