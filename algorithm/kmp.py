#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
"""
   python 实现kmp 算法
   返回第一次出现的指定子字符串在源字符串中的索引
"""
def index(source, target, pos):
    """
    在源字符串source中，查找目标字符串target。从pos位置开始查找
    朴素算法：（时间复杂度为O(m*n)，m为源串的长度，n为目标串的长度）
        1、从源字符串中，逐个字符与目标字符串比较。如果相等，则返回当前字符串的位置
        2、如果不相等，则从源字符串的下一个位置开始，与目标字符串逐个比较
    :param source str: 源字符串
    :param target str: 目标字符串
    :param pos int: 查找位置
    :return 目标字符串在源字符串中的第一个位置
    """
    if not source or not target:
        return -1
    index = -1
    ls = len(source)
    lt = len(target)
    while pos < ls and lt + pos <= ls:
        flag = True
        for i in range(lt):
            if source[pos + i] != target[i]:
                pos += 1
                flag = False
                break
        if flag:
            return pos
    return index

def kmp_pmt(target):
    """
    部分匹配表的最大元素长度
    部分匹配表(Partial Match Table)
    "部分匹配值"就是"前缀"和"后缀"的最长的共有元素的长度。以"ABCDABD"为例，
    －　"A"的前缀和后缀都为空集，共有元素的长度为0；
    －　"AB"的前缀为[A]，后缀为[B]，共有元素的长度为0；
    －　"ABC"的前缀为[A, AB]，后缀为[BC, C]，共有元素的长度0；
    －　"ABCD"的前缀为[A, AB, ABC]，后缀为[BCD, CD, D]，共有元素的长度为0；
    －　"ABCDA"的前缀为[A, AB, ABC, ABCD]，后缀为[BCDA, CDA, DA, A]，共有元素为"A"，长度为1；
    －　"ABCDAB"的前缀为[A, AB, ABC, ABCD, ABCDA]，后缀为[BCDAB, CDAB, DAB, AB, B]，共有元素为"AB"，长度为2；
    －　"ABCDABD"的前缀为[A, AB, ABC, ABCD, ABCDA, ABCDAB]，后缀为[BCDABD, CDABD, DABD, ABD, BD, D]，共有元素的长度为0。
    """
    prefix = [target[:i+1] for i in range(len(target) - 1)]
    suffix = [target[i+1:] for i in range(len(target) - 1)]
    common = list(set(prefix) & set(suffix))
    if common:
        cmn = map(len, common)
        return max(cmn)
    return 0

def kmp_index(source, target, pos):
    """
    在源字符串source中，查找目标字符串target。从pos位置开始查找
        参考：http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html

    KMP算法中，引入了前缀函数的概念，从而可以更加精确的知道：当不匹配发生时，应该跳过多少个字符。
    KMP算法：时间复杂度为O(m+n)，m为源串的长度，n为目标串的长度
    移动位数 = 已匹配的字符数 - 对应的部分匹配值
    """
    index = -1
    if not source or not target:
        return index
    ls = len(source)
    lt = len(target)
    while pos < ls and lt + pos <= ls:
        match = True
        for i in range(lt):
            if source[pos + i] != target[i]:
                match = False
                break
        if match:
            return pos
        # 移动位数 = 已匹配的字符数 – 对应的部分匹配值
        if i:
            # 用于生成部分匹配表
            tar = target[:i]
            pos += i - kmp_pmt(tar)
        else:
            pos += 1
    return index

if __name__ == '__main__':

    source = 'abcdabcdabde'
    target = 'abcdabd'
    pos = 0

    print '-'*20 + '朴素算法' + '-'*20
    print u'源字符串为：%s, 目标字符串为：%s, 从 %s 位置处开始查找' %(source, target, pos) 
    ind = index(source, target, pos)
    print u'查询到目标字符串的位置为：%s' %ind

    print '-'*20 + 'KMP算法' + '-'*20
    print u'源字符串为：%s, 目标字符串为：%s, 从 %s 位置处开始查找' %(source, target, pos) 
    ind = kmp_index(source, target, pos)
    print u'查询到目标字符串的位置为：%s' %ind

