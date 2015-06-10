#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
给定一个整数n，返回n!（n的阶乘）数字中的后缀0的个数。
给定N，求N！的末尾有多少0。要求算法复杂度为lg
注意：你的解法应该满足多项式时间复杂度。

Input: n = 5
Output: 1 
Factorial of 5 is 20 which has one trailing 0.

Input: n = 20
Output: 4
Factorial of 20 is 2432902008176640000 which has
4 trailing zeroes.

Input: n = 100
Output: 24
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        """ 
            O(n) 的时间复杂度
            n! n的阶乘，然后计算数字后缀为0的个数 
        """
        res = reduce(lambda x,y: x*y, range(1, n+1))
        i = 0
        while res > 0:
            if res % 10 == 0:
                i += 1
            res = res / 10
            if res % 10 != 0:
                break
        return i

    def trailingZeroes2(self, n):
        """ 
            O(logn)的时间复杂度
            n! 中0的个数，表示为 （2*5）的个数。
            后缀0总是由质因子2和质因子5相乘得来的。
            所以对N!进行素数分解：N！=2^i****5^j***.
            则末尾0的个数为min(i,j). 又由于i明显远大于j，所以我们只要求解j即可。
            又j均由1-N中5的倍数所提供，如果该数仅为5的倍数则贡献1，若为25的倍数则贡献2. 
            [n/k]代表1~n中能被k整除的个数
        """
        x = 5
        ans = 0
        while n >= x:
            ans += n / x
            x *= 5
        return ans

    def trailingZeroes3(self, n):
        """ O(logn)的时间复杂度，递归调用 """
        return 0 if n < 5 else n/5 + self.trailingZeroes(n/5)

if __name__ == '__main__':
    sol = Solution()
    n = 16
    
    start_time = time.time()
    result = sol.trailingZeroes(n)
    use_time = time.time() - start_time

    print '-'*20 + 'Rotate Array' + '-'*20
    print u'n：%s，n的阶乘中，后缀为0的个数是：%s ' %(n, result)
    print u'耗时：%s' %use_time

    start_time = time.time()
    result = sol.trailingZeroes2(n)
    use_time = time.time() - start_time

    print '-'*20 + 'Rotate Array' + '-'*20
    print u'n：%s，n的阶乘中，后缀为0的个数是：%s ' %(n, result)
    print u'耗时：%s' %use_time

    start_time = time.time()
    result = sol.trailingZeroes3(n)
    use_time = time.time() - start_time

    print '-'*20 + 'Rotate Array' + '-'*20
    print u'n：%s，n的阶乘中，后缀为0的个数是：%s ' %(n, result)
    print u'耗时：%s' %use_time

