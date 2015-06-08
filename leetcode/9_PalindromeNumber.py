#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
确定一个整数是否是回文
有这样一类数字，它们顺着看和倒着看是相同的数，例如121、656、2332等，这样的数字叫做回文数字
"""
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x):
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) / 10
            ranger /= 100
        return True


if __name__ == '__main__':
    sol = Solution()
    source = 1234321
    
    start_time = time.time()
    result = sol.isPalindrome2(source)
    use_time = time.time() - start_time

    print u'是否回文，原始字符串为: %s, 是否回文： %s' %(source, result)
    print u'耗时：%s' %use_time

