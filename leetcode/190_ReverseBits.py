#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Reverse Bits

Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

十进制转二进制：bin()
十进制转八进制：oct()
十进制转十六进制：hex()

二进制转十进制：int(n, base=2)
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)
        return int('0b' + b[2:][::-1] + '0'*(32-len(b[2:])), 2)

    def reverseBits2(self, n):
        """ ljust(width, '0')右补齐 """
        x = bin(n)[:1:-1].ljust(32,'0')
        return int(x, base = 2)

    def reverseBits3(self, n):
        """ 左边填充，zfill(width) """
        return int(bin(n)[2:].zfill(32)[::-1],2)

if __name__ == '__main__':
    sol = Solution()

    n = 43261596
    
    start_time = time.time()
    result = sol.reverseBits(n)
    use_time = time.time() - start_time

    print '-'*20 + 'Number Of 1 Bits' + '-'*20
    print u'n：%s，反转2进制数为：%s ' %(n, result)
    print u'耗时：%s' %use_time

