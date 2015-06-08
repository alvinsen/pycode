#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
String to Integer (atoi)
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, 
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). 
You are responsible to gather all the input requirements up front.

atoi()函数的功能：将字符串转换成整型数；atoi()会扫描参数nptr字符串，跳过前面的空格字符，
直到遇上数字或正负号才开始做转换，而再遇到非数字或字符串时（'\0'）才结束转化，并将结果返回（返回转换后的整型数）。

"""
class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, source):
        lst = []
        symbol = 1
        for ch in source:
            if ch == '-' and not lst:
                symbol = -1
            if ch > '0' and ch < '9':
                lst.append(ch)

            if not lst:
                continue
            if lst and ch not in map(str, range(9)):
                break
        return symbol * int(''.join(lst))


if __name__ == '__main__':
    sol = Solution()
    source = 'abc-2342343.233'
    
    start_time = time.time()
    result = sol.myAtoi(source)
    use_time = time.time() - start_time

    print u'ATOI函数，原始字符串为: %s, 转换后的int数据位： %s' %(source, result)
    print u'耗时：%s' %use_time

