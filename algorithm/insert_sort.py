#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
"""
    python 实现插入排序
"""
def insert_sort(lis):
    """
    python 实现插入排序, 升序排序：时间复杂度O(n**2)
    1、从第一个元素开始，该元素可以认为已经被排序
    2、取出下一个元素，在已经排序的元素序列中从后向前扫描
    3、如果该元素（已排序）大于新元素，将该元素移到下一位置
    4、重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    5、将新元素插入到该位置后
    6、重复步骤2~5
    """
    a_list = lis[:]
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    
    use_time = time.time() - start_time
    print '插入排序后结果为：%s, 耗时：%s' %(a_list, use_time)


def binary_insert_sort(lis):
    """
    python 实现二分插入排序，升序 
    1、从第一个元素开始，该元素可以认为已经被排序
    2、取出下一个元素，在已经排序的元素序列中二分查找到第一个比它大的数的位置
    3、将新元素插入到该位置后
    4、重复上述两步
    """
    a_list = lis[:]
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        low = 0
        high = index-1
        ### 开始查找待插入记录的正确位置
        while low <= high:
            mid = (low + high) / 2
            if a_list[mid] > current_value:
                high = mid - 1
            else:
                low = mid + 1
        ### 将前面所有大于当前待插入记录的记录后移
        while position > low:
            a_list[position] = a_list[position - 1]
            position = position -1
        ### 将待插入记录 回填到正确位置
        a_list[position] = current_value
    use_time = time.time() - start_time
    print '二分插入排序后结果为：%s, 耗时：%s' %(a_list, use_time)


if __name__ == '__main__':
    lst = random.sample(xrange(100), 10)

    print u'待排序序列为：%s' %(lst) 
    insert_sort(lst)
    print '-'*50
    binary_insert_sort(lst)
