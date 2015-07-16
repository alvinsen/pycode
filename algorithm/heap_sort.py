#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
python 实现堆排序
"""
def heap_adjust(mylist, start, end):
    """
    堆调整
    """
    left = 0  
    right = 0  
    maxv = 0  
    left = start * 2  
    right = start * 2 + 1  
    while left <= end:  
        maxv = left  
        if right <= end:  
            if mylist[left] < mylist[right]:  
                maxv = right  
            else:  
                maxv = left  
        if mylist[start] < mylist[maxv]:  
            tmp = mylist[maxv]  
            mylist[maxv] = mylist[start]  
            mylist[start] = tmp  
            start = maxv  
        else:  
            break  
        left = start * 2  
        right = start * 2 + 1

def build_heap(mylist):
    """
    构建堆
    """
    size = len(mylist)  
    i = (size -1) // 2;  
    while i >= 0:  
        heap_adjust(mylist, i, size - 1)  
        i = i - 1  

def heap_sort(mylist):
    """
    python 实现堆排序
    堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
    堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
    1、在对应的数组元素A[i], 左孩子A[LEFT(i)], 和右孩子A[RIGHT(i)]中找到最大的那一个，将其下标存储在largest中。
        其中：LEFT(i) = 2*i，RIGHT(i) = 2*i + 1
    2、如果A[i]已经就是最大的元素，则程序直接结束。
    3、否则，i的某个子结点为最大的元素，将A[largest]与A[i]交换。
    4、再从交换的子节点开始，重复1,2,3步，直至叶子节点，算完成一次堆调整。
    """
    # 构建堆
    build_heap(mylist)
    i = len(mylist) - 1
    while i >= 0:  
        mylist[0], mylist[i] = mylist[i], mylist[0]  
          
        heap_adjust(mylist, 0, i - 1)  
        i = i - 1

mylist0 = [11, 23, 1, 24, 112, 200, 9, 32]
print '++++++++python 实现堆排序，原数组为：%s' %mylist0
heap_sort(mylist0)  
print '排序后的数组为：%s' %mylist0
