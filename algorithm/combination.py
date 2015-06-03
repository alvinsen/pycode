#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
全组合问题：
所谓全组合，就是打印出字符串中所有字符的所有组合。
还是输入三个字符 a、b、c，则它们的组合有a b c ab ac bc abc。
当然我们还是可以借鉴全排列的思路，利用问题分解的思路，最终用递归解决。不过这里介绍一种比较巧妙的思路 —— 基于位图。
字符串长度为 n， 则全组合的个数为：pow(2,n)−1

位操作方法：假设元素原本有：a,b,c 三个，则 1 表示取该元素，0 表示不取。
故取 a 则是001，取 ab 则是011， abc 则是 111。所以一共三位，每个位上有两个选择 0 和 1。而 000 没有意义，所以是 pow(2,n)−1 个结果。
"""

def combination(arr):
    """
        位操作法实现全组合
    """
    if not arr:
        return
    ln = len(arr)
    if ln == 1:
        print u'长度为1，排列为：%s' %arr
        return arr
    # 相当于 pow(2, ln)
    n = 1 << ln
    ### 从 1 循环到 pow(2, ln) - 1
    for i in range(1, n):
        arr_list = []
        for j in range(ln):
            temp = i 
            if temp & (1 << j):
                ### 对应位上为1， 则输出对应的字符
                arr_list.append(arr[j])

        print u'组合为：%s' %(arr_list) 


if __name__ == '__main__':

    lst = ['a','b','c']
    combination(lst)

