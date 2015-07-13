#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
"""
   python 实现冒泡排序
"""
def bubble_sort(lst):
    """
    python 实现冒泡排序：时间复杂度O(n**2)
    1、每个回合都从第一个元素开始和它后面的元素比较，如果比它后面的元素更大的话就交换，一直重复，直到这个元素到了它能到达的位置。
    2、每次遍历都将剩下的元素中最大的那个放到了序列的“最后”(除去了前面已经排好的那些元素)。
    注意检测是否已经完成了排序，如果已完成就可以退出了。
    """
    need_sort_list = lst[:]
    size = len(need_sort_list)

    start_time = time.time()
    for i in xrange(size):
        for j in xrange(size - 1):
            if need_sort_list[j] > need_sort_list[j+1]:
                need_sort_list[j], need_sort_list[j+1] = need_sort_list[j+1], need_sort_list[j]
    use_time = time.time() - start_time
    print '冒泡排序后结果为：%s, 耗时：%s' %(need_sort_list, use_time)
    print '---------------------------------------------------------'

    need_sort_list = lst[:]
    start_time2 = time.time()
    for i in range(size):
        for j in range(size - 1):
            if need_sort_list[j] > need_sort_list[j+1]:
                need_sort_list[j], need_sort_list[j+1] = need_sort_list[j+1], need_sort_list[j]
    use_time2 = time.time() - start_time2
    print '冒泡排序后结果为：%s, 耗时：%s' %(need_sort_list, use_time2)
    print '---------------------------------------------------------'

    need_sort_list = lst[:]
    start_time3 = time.time()
    for i in xrange(size):
        for j in xrange(size-1-i):
            if need_sort_list[j] > need_sort_list[j+1]:
                need_sort_list[j], need_sort_list[j+1] = need_sort_list[j+1], need_sort_list[j]
    use_time3 = time.time() - start_time3
    print '冒泡排序后结果为：%s, 耗时：%s' %(need_sort_list, use_time3)
    print '---------------------------------------------------------'


if __name__ == '__main__':

    lst = random.sample(xrange(100), 10)

    print '待排序序列为：%s' %(lst) 
    bubble_sort(lst)
