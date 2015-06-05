#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Happy Number

Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

快乐数：该数字所有数位(digits)的平方和，得到的新数继续求所有数位的平方和，最终结果必为1
非快乐数：在循环求平方和的过程中，会出现重复

Example: 19 is a happy number

pow(1,2) + pow(9,2) = 82
pow(8,2) + pow(2,2) = 68
pow(6,2) + pow(8,2) = 100
pow(1,2) + pow(0,2) + pow(0,2) = 1
"""
# Definition for singly-linked list.
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        dic = {}
        dic[n] = 1
        def sum_squares(n):
            temp = map(lambda x:pow(int(x),2), list(str(n)))
            n = reduce(lambda x,y: x+y, temp)
            return n

        while True:
            n = sum_squares(n)
            if n == 1:
                return True
            if dic.get(n, None):
                return False
            dic[n] = 1

    def isHappy2(self, n):
        cycle = set()
        while n!=1 and n not in cycle:
            cycle.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1

if __name__ == '__main__':
    sol = Solution()

    n = 19
    n2 = 37

    # start_time = time.time()
    # result = sol.isHappy(n)
    # use_time = time.time() - start_time

    # print '-'*20 + '判断是否快乐数' + '-'*20
    # print u'数字为：%s，是否快乐数：%s ' %(n, result)
    # print u'耗时：%s' %use_time

    # start_time = time.time()
    # result = sol.isHappy(n2)
    # use_time = time.time() - start_time

    # print '-'*20 + '判断是否快乐数' + '-'*20
    # print u'数字为：%s，是否快乐数：%s ' %(n2, result)
    # print u'耗时：%s' %use_time

    start_time = time.time()
    result = sol.isHappy2(n2)
    use_time = time.time() - start_time

    print '-'*20 + '判断是否快乐数' + '-'*20
    print u'数字为：%s，是否快乐数：%s ' %(n2, result)
    print u'耗时：%s' %use_time
