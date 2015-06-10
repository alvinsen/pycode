#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Excel Sheet Column Number
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

"""
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        """ 相当于26进制 """
        res = 0
        for k, v in enumerate(list(s)):
            val = pow(26, len(s) - k - 1) * (ord(v) - ord('A') + 1)
            res += val
        return res

    def titleToNumber2(self, s):
        """  """
        ### return reduce(lambda r, c: 26*r + ord(c)-64, s, 0)
        return reduce(lambda x,y: x*26+y, (ord(c)-64 for c in s))

    def titleToNumber3(self, s):
        return sum([j*26**i for i, j in enumerate(map(lambda x:ord(x)-64, s[::-1]))])


if __name__ == '__main__':
    sol = Solution()
    title = 'AB'
    
    start_time = time.time()
    result = sol.titleToNumber(title)
    use_time = time.time() - start_time

    print '-'*20 + 'Rotate Array' + '-'*20
    print u'excel中列名为：%s，列名转换为数字是：%s ' %(title, result)
    print u'耗时：%s' %use_time

    start_time = time.time()
    result = sol.titleToNumber2(title)
    use_time = time.time() - start_time

    print '-'*20 + 'Rotate Array' + '-'*20
    print u'excel中列名为：%s，列名转换为数字是：%s ' %(title, result)
    print u'耗时：%s' %use_time


    start_time = time.time()
    result = sol.titleToNumber3(title)
    use_time = time.time() - start_time

    print '-'*20 + 'Rotate Array' + '-'*20
    print u'excel中列名为：%s，列名转换为数字是：%s ' %(title, result)
    print u'耗时：%s' %use_time
