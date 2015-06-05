#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Number Of 1 Bits

Write a function that takes an unsigned integer and 
returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has 
binary representation 00000000000000000000000000001011, so the function should return 3.

十进制转二进制：bin()
十进制转八进制：oct()
十进制转十六进制：hex()

"""
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        b = bin(n)
        return b.count('1')

    def hammingWeight2(self, n):
        a = 0;
        while n:
            if n % 2: 
                a += 1
            n = n / 2;
        return a

    def hammingWeight3(self, n):
        return sum([int(x) for x in str(bin(n))[2:]])

if __name__ == '__main__':
    sol = Solution()

    n = 11
    
    start_time = time.time()
    result = sol.hammingWeight(n)
    use_time = time.time() - start_time

    print '-'*20 + 'Number Of 1 Bits' + '-'*20
    print u'n：%s，二进制数中1的位数：%s ' %(n, result)
    print u'耗时：%s' %use_time


    start_time = time.time()
    result = sol.hammingWeight2(n)
    use_time = time.time() - start_time

    print '-'*20 + 'Number Of 1 Bits' + '-'*20
    print u'n：%s，二进制数中1的位数：%s ' %(n, result)
    print u'耗时：%s' %use_time
