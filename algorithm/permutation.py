#!/usr/bin/python
# -*- coding:utf-8 -*-
import copy
"""
全排列问题：
所谓全排列，就是打印出字符串中所有字符的所有排列。
例如输入字符串abc，则打印出 a、b、c 所能排列出来的所有字符串 abc、acb、bac、bca、cab 和 cba 。

字符串长度为 n， 则全排列的个数为： n!
"""

total = 0
def pernutation(array, start, end):
    """
        全排列的递归实现
    """
    global total
    if start == end:
        total += 1
        print u'排列为：%s, 第 %s 个 ' %(array, total)
    else:

        for i in xrange(start, end+1):
            array[start], array[i] = array[i], array[start]
            pernutation(array, start+1, end)
            array[start], array[i] = array[i], array[start]

no_repeat_total = 0
def pernutation_no_repeat(array, start, end):
    """
        全排列的递归实现之去重
    """
    def isSwap(arr, start, end):
        # 在 arr 数组中，[start,end) 中是否有与 arr[end] 元素相同的
        while start < end:
            if arr[start] == arr[end]:
                return False
            start += 1
        return True
    global no_repeat_total
    if start == end:
        no_repeat_total += 1
        print u'去重排列为：%s, 第 %s 个 ' %(array, no_repeat_total)
    else:

        for i in xrange(start, end+1):
            if isSwap(array, start, i):
                array[start], array[i] = array[i], array[start]
                pernutation_no_repeat(array, start+1, end)
                array[start], array[i] = array[i], array[start]


def un_pernutation(arr):
    """
        全排列的非递归实现, 即按字典序排列算法
        1.对初始队列进行排序，找到所有排列中最小的一个排列Pmin。
        2.找到刚刚好比Pmin大比其它都小的排列P(min+1)。
        3.循环执行第二步,直到找到一个最大的排列,算法结束。

        算法如下：
        给定已知序列P =  A1A2A3.....An
        对P按字典排序，得到P的一个最小排列Pmin = A1A2A3....An ，满足Ai > A(i-1) (1 < i <= n)
        从Pmin开始,找到刚好比Pmin大的一个排列P(min+1)，再找到刚好比P(min+1)大的一个排列，如此重复。
        1.从后向前（即从An->A1）,找到第一对为升序的相邻元素，即Ai < A(i+1)。
          若找不到这样的Ai，说明已经找到最后一个全排列，可以返回了。
        2.从后向前,找到第一个比Ai大的数Aj，交换Ai和Aj。
        3.将排列中A(i+1)A(i+2)....An这个序列的数逆序倒置，即An.....A(i+2)A(i+1)。
            因为由前面第1、2可以得知，A(i+1)>=A(i+2)>=.....>=An,这为一个升序序列，应将该序列逆序倒置，
            所得到的新排列才刚刚好比上个排列大。
        4.重复步骤1-3,直到返回。
    """
    ln = len(arr)
    if ln == 1:
        print u'长度为1，排列为：%s' %arr
        return [arr]

    ### 字典升序排序，一直到字典降序排序终止。最大为序列长度的阶乘。。。
    ### 1、找到升序序列，Pmin = A1A2A3...An,满足 Ai > A(i-1)
    array = copy.deepcopy(arr)
    array.sort()

    result = []
    first = array[:]
    result.append(first)

    ### 求序列的阶乘
    total = reduce(lambda x,y: x*y, range(1, ln + 1))
    for i in range(total):

        ### 1、从后向前，找到 前一个 > 后一个 ——》 Ai > A(i+1)
        minIndex = ln - 2
        while minIndex > 0:
            if array[minIndex] < array[minIndex + 1]:
                break
            minIndex -= 1

        ### 2、从后向前到第1步中找到的i，找到第一个比Ai大的数Aj, 交换Ai 和Aj。
        ###    找到刚好比 minIndex 大的数 maxIndex
        maxIndex = ln - 1
        while maxIndex > minIndex:
            if array[maxIndex] > array[minIndex]:
                break
            maxIndex -= 1
        array[minIndex], array[maxIndex] = array[maxIndex], array[minIndex]

        ### 由于前两个循环会导致 minIndex == maxIndex == 0， 这里需要处理一下
        if minIndex == maxIndex == 0:
            continue

        ### 3、逆置序列： 逆置 minIndex 后面的序列
        arr_left = array[:minIndex+1]
        arr_right = array[minIndex+1:]
        arr_right = list(reversed(arr_right))

        array = arr_left + arr_right 
        tmp_arr = copy.deepcopy(array)
        result.append(tmp_arr)

    return result

if __name__ == '__main__':

    lst = [1,2,2]
    pernutation(lst, 0, len(lst) - 1)
    pernutation_no_repeat(lst, 0, len(lst) - 1)
    result = un_pernutation(lst)

    print u'非递归的全排列为：'
    for x in result:
        print '%s' %x

