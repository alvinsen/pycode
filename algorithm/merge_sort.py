#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
"""
    python 实现合并排序
"""
def merge_sort(lis):
    """
    python 实现合并排序, 升序排序：时间复杂度O(nlogn)
    
    典型的是二路合并排序，将原始数据集分成两部分(不一定能够均分)，分别对它们进行排序，
    然后将排序后的子数据集进行合并，这是典型的分治法策略。
    """
    def merge_sort_split(a_list):
        # print "Splitting: ", a_list
        if len(a_list) > 1:
            mid = len(a_list) // 2
            left_half = a_list[:mid]
            right_half = a_list[mid:]
            merge_sort_split(left_half)
            merge_sort_split(right_half)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    a_list[k] = left_half[i]
                    i += 1
                else:
                    a_list[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                a_list[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                a_list[k] = right_half[j]
                j += 1
                k += 1
        # print "Merging: ", a_list

    a_list = lis[:]
    start_time = time.time()
    merge_sort_split(a_list)
    
    use_time = time.time() - start_time
    print '合并结果为：%s, 耗时：%s' %(a_list, use_time)


if __name__ == '__main__':
    lst = random.sample(xrange(100), 10)

    print u'待排序序列为：%s' %(lst) 
    merge_sort(lst)
