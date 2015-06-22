#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
"""
    python 实现快速排序
    快速排序的思想：
    快速排序采用的思想是分治思想。
    快速排序是找出一个元素（理论上可以随便找一个）作为基准(pivot), 然后对数组进行分区操作, 
    使基准左边元素的值都不大于基准值, 基准右边的元素值 都不小于基准值，如此作为基准的元素调整到排序后的正确位置。
    递归快速排序，将其他n-1个元素也调整到排序后的正确位置。最后每个元素都是在排序后的正确位置，排序完成。
    所以快速排序算法的核心算法是分区操作，即如何调整基准的位置以及调整返回基准的最终位置以便分治递归。

假设要排序的序列为：
【2】 list: 2 4 9 3 6 7 1 5 首先用2当作基准，使用i j两个指针分别从两边进行扫描，把比2小的元素和比2大的元素分开。
                            首先比较2和5，5比2大，j左移

【2】 list: 2 4 9 3 6 7 1 5 比较2和1，1小于2，所以把1放在2的位置

【2】 list: 1 4 9 3 6 7 1 5 比较2和4，4大于2，因此将4移动到后面

【2】 list: 1 4 9 3 6 7 4 5 比较2和7，2和6，2和3，2和9，全部大于2，满足条件，因此不变

经过第一轮的快速排序，元素变为下面的样子
[1] 2 [4 9 3 6 7 5]
"""
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list)-1)

def quick_sort_helper(a_list, left, right):
    """
        1、从第一个元素开始，该元素可以认为已经被排序
        2、
    """
    if left < right:
        split_point = partition(a_list, left, right)
        quick_sort_helper(a_list, left, split_point)
        quick_sort_helper(a_list, split_point+1, right)

def partition(a_list, left, right):
    """
    1、将left 作为基准值
    2、如果 right 位置的值，比基准值大，则从right 向左移动，right -= 1。否则将 right 的值，赋值给left
    3、如果 left 位置的值， 比基准值小，则从left  向左移动， left += 1。否则将 left  的值，赋值给right
    4、如果 left < right， 重复 第二、三步
    5、将基准值， 赋值给low
    6、基准值 左右两边递归调用上述过程。。。
    """
    pivot_val = a_list[left]
    low, high = left, right
    while low < high:
        while a_list[high] > pivot_val and low < high:
            high -= 1
        if low < high:
            a_list[low] = a_list[high]
        while a_list[low] < pivot_val and low < high:
            low += 1 
        if low < high:
            a_list[high] = a_list[low]
    a_list[low] = pivot_val
    return high

if __name__ == '__main__':

    # lst = random.sample(xrange(100), 10)
    lst = [x for x in range(10)]
    # 随机打散
    random.shuffle(lst)

    print '***' * 50 

    a_list = lst[:]
    print u'待排序序列为：%s' %(a_list)
    quick_sort(a_list)
    print '已排序序列：a_list: %s' %a_list

