#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Plus One
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.

"""
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        new = []
        plus_one = 1
        for val in digits[::-1]:
            temp = val + plus_one
            plus_one = val // 10
            new.append(temp % 10)

        if plus_one == 1:
            new.append(plus_one)

        return list(reversed(new))
    
    def plusOne2(self, digits):
        num = 0
        for k, val in enumerate(digits[::-1]):
            num += pow(10, k) * int(val)    
        num += 1
        return [int(v) for v in str(num)]

    def plusOne3(self, digits):
        return map(int,list(str(int(''.join(map(str,digits)))+1)))




if __name__ == '__main__':
    sol = Solution()
    digits = [3,0,9,9]

    start_time = time.time()
    result = sol.plusOne(digits)
    use_time = time.time() - start_time

    print '-'*40
    print u'数组为：%s, 加一后数组为：%s' %(digits, result)
    print u'耗时：%s' %use_time

    start_time = time.time()
    result = sol.plusOne2(digits)
    use_time = time.time() - start_time

    print '-'*40
    print u'数组为：%s, 加一后数组为：%s' %(digits, result)
    print u'耗时：%s' %use_time

    