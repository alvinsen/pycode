#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

"""
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        """ 相当于27进制，满27才进1 """
        lst = []
        while n > 0:
            k = n % 26
            n = n / 26
            if k == 0 and n > 0:
                lst.append(chr(ord('A') + 25))
                n = n - 1
            else:
                lst.append(chr(ord('A') + k - 1))
        lst.reverse()
        return ''.join(lst)

    def convertToTitle(self, n):
        r = ''
        while(n>0):
            n -= 1
            r = chr(n%26+65) + r
            n /= 26
        return r

    def convertToTitle(self, n):
        s = ''
        while num:
            temp = num % 26
            if not temp:
                s += 'Z'
                num = num/26-1
            else:
                s += chr(temp+64)
                num /= 26
        return s[::-1]


if __name__ == '__main__':
    sol = Solution()
    
    result = 26
    start_time = time.time()
    title_result = sol.convertToTitle(result)
    use_time = time.time() - start_time

    print '-'*20 + 'Rotate Array' + '-'*20
    print u'excel中数字为：%s, 对应的列名为：%s ' %(result, title_result)
    print u'耗时：%s' %use_time

