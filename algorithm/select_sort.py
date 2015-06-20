#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
"""
    python 实现选择排序
    选择排序，可以选择最大的元素，或者最小的元素进行排序。最小的元素向前移动，最大的元素向后移动
"""
def select_sort(lst):
    """
    python 实现选择排序算法： 时间复杂度O(n**2)
    1、初始状态：无序区为R[1..n]，有序区为空。
    2、第i趟排序(i=1,2,3...n-1)
        第i趟排序开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。
        该趟排序从当前无序区中选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，
        使R[1..i]和R分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区。
    3、前n-1趟结束，数组有序化了

    在插入和选择排序中，若初始数据基本正序，则选用 插入排序（到尾部）   ；若初始数据基本反序，则选用   选择排序 。

    选择排序：每个回合都选择出剩下的元素中最大的那个，选择的方法是首先默认第一元素是最大的，
    如果后面的元素比它大的话，那就更新剩下的最大的元素值，找到剩下元素中最大的之后将它放入到合适的位置就行了。
    和冒泡排序类似，只是找剩下的元素中最大的方式不同而已。
    """
    # 第一种方式，从前向后比较，将最小的移动到最前面
    start_time = time.time()
    need_sort_list = lst[:]
    n = len(need_sort_list)
    for i in xrange(n):
        min_index = i
        for j in xrange(i+1, n):
            if need_sort_list[min_index] > need_sort_list[j]:
                min_index = j
        if min_index != i:
            need_sort_list[i], need_sort_list[min_index] = need_sort_list[min_index], need_sort_list[i]

    use_time = time.time() - start_time
    print '选择排序后结果为：%s, 耗时：%s' %(need_sort_list, use_time)

    # 另一种方式：从后向前比较    
    # start_time = time.time()
    # for fill_slot in range(len(a_list) - 1, 0, -1):
    #     pos_of_max = 0
    #     for location in range(1, fill_slot + 1):
    #         if a_list[location] > a_list[pos_of_max]:
    #             pos_of_max = location
        
    #     a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]

if __name__ == '__main__':

    lst = random.sample(xrange(100), 10)

    print u'待排序序列为：%s' %(lst) 
    select_sort(lst)
