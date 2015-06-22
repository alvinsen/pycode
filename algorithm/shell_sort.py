#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
"""
    python 实现希尔排序
"""
def shell_sort(lis):
    """
    python 实现希尔排序，也叫递减增量排序
    1、先取一个小于n的整数d1作为第一个增量，把文件的全部记录分成d1个组。
    2、所有距离为d1的倍数的记录放在同一个组中，在各组内进行直接插入排序。
    3、取第二个增量d2<d1重复上述的分组和排序，
    4、直至所取的增量dt=1(dt<dt-l<…<d2<d1)，即所有记录放在同一组中进行直接插入排序为止。 

    不是很懂。。。
    """
    need_sort_list = lis[:]
    # 增量, 分成3个组
    gap = 0
    n = len(need_sort_list)
    start_time = time.time()
    while gap <= n:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, n):
            j = i - gap
            temp = need_sort_list[i]
            while j >= 0 and need_sort_list[j] > temp:
                need_sort_list[j+gap] = need_sort_list[j]
                j = j - gap
            need_sort_list[j+gap] = temp
        gap = (gap - 1) / 3
    use_time = time.time() - start_time
    print '希尔排序后结果为：%s, 耗时：%s' %(need_sort_list, use_time)

def myself_shell_sort(lst):
    """
        希尔排序
        第一次增量为： len(a_list)/2， 分成两个组，每个组对应位置进行对比，如果第一组小于第二组，则进行交换
        第二次增量为： len(a_list)/3， 分成三个组，每个组对应位置进行对比，如果第二组小于第三组，则进行交换，如果第一组小于第二组，则进行交换
        依次进行排序， 直到增量为：1
    """
    a_list = lst[:]
    start_time = time.time()

    length = len(a_list)
    gap = length // 2
    while gap > 0:
        for last_i in range(gap, length):
            first_i = last_i - gap
            temp = a_list[last_i]
            while first_i >= 0 and a_list[first_i] > temp:
                a_list[first_i + gap] = a_list[first_i]
                first_i = first_i - gap
            a_list[first_i + gap] = temp
        gap -= 1

    use_time = time.time() - start_time
    print '希尔排序后结果为：%s, 耗时：%s' %(a_list, use_time)


if __name__ == '__main__':
    lst = random.sample(xrange(100), 10)
    alist = lst[:]

    print u'待排序序列为：%s' %(lst) 
    shell_sort(alist)

    print '-'*50
    print u'待排序序列为：%s' %(lst) 
    myself_shell_sort(alist)

