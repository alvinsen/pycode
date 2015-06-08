#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Reverse Integer
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        """ 基本实现，没有考虑任何int 溢出问题，以及 100 这类问题 """
        flag = False
        if x > 0:
            flag = True
        lst = map(int, list(str(abs(x))))
        lst.reverse()
        return int(''.join(map(str, lst))) if flag else -int(''.join(map(str, lst)))

    def reverse2(self, x):
        """  """
        symbol = True
        if x < 0:
            symbol = -1
        lst = map(int, list(str(abs(x))))
        lst.reverse()
        result = int(''.join(map(str, lst)))
        return 0 if result > pow(2, 31) else result * symbol

    def reverse3(self, x):
        """  """
        result = 0
        symbol = 1
        if x < 0:
            symbol = -1

        x = abs(x)
        while x:
            result = result * 10 + x % 10
            x /= 10

        return 0 if result > pow(2, 31) else result * symbol

    def reverse4(self, x):
        negFlag = 1
        if x < 0:
            negFlag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1])
        return 0 if x > pow(2, 31) else x * negFlag

    def reverse5(self, x):
        revx = int(str(abs(x))[::-1]) #reverse the abs(x) and convert to int
        return 0 if revx>math.pow(2,31) else revx * cmp(x,0)


if __name__ == '__main__':
    sol = Solution()
    x = -123

    start_time = time.time()
    result = sol.reverse(x)
    use_time = time.time() - start_time

    print u'原数字为：%s, 反转后的数字为：%s' %(x, result)
    print u'耗时：%s' %use_time

