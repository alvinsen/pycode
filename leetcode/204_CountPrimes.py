#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import math
"""
Count Primes
Description:
Count the number of prime numbers less than a non-negative number, n.
求小于 n 的素数的个数

Hint:
Let's start with a isPrime function. 
To determine if a number is prime, we need to check if it is not divisible by any number less than n. 
The runtime complexity of isPrime function would be O(n) and hence counting 
the total prime numbers up to n would be O(n2). Could we do better?
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        """
            求 n 以内的素数
        """
        result = []
        for i in range(2, n):
            flag = True
            for j in range(2, int(math.sqrt(n))+1):
                if i % j == 0 and i != j:
                    flag = False
                    break
            if flag:
                result.append(i)
        return (len(result), result)

    def countPrimes2(self, n):
        """
            筛素数法
        """
        primes = {}
        flags = [False] * n
        index = 0
        for i in range(2, n):
            if not flags[i]:
                primes[index] = i
                index += 1
            j = 0
            while j < index and i * primes[j] < n:
                flags[i * primes[j]] = True
                j += 1
        result = primes.values()
        return (len(result), result)

    def countPrimes3(self, n):
        """
            筛素数法
        """
        primes = {}
        flags = [False] * n
        index = 0
        for i in range(2, n):
            if not flags[i]:
                primes[index] = i
                index += 1
            j = 0
            while j < index and i * primes[j] < n:
                flags[i * primes[j]] = True
                ### 确保每个数只被筛选一次
                if i % primes[j] == 0:
                    break
                j += 1
        result = primes.values()
        return (len(result), result)

    def countPrimes4(self, n):
        """
            筛素数法
        """
        pass

if __name__ == '__main__':
    sol = Solution()
    n = 10

    start_time = time.time()
    result = sol.countPrimes(n)
    use_time = time.time() - start_time

    print '-'*40
    print u'n：%s 以内素数为：%s， 个数为：%s' %(n, result[1], result[0])
    print u'耗时：%s' %use_time

    # start_time = time.time()
    # result = sol.countPrimes2(n)
    # use_time = time.time() - start_time

    # print '-'*40
    # print u'n：%s 以内素数为：%s， 个数为：%s' %(n, result[1], result[0])
    # print u'耗时：%s' %use_time

    # start_time = time.time()
    # result = sol.countPrimes3(n)
    # use_time = time.time() - start_time

    # print '-'*40
    # print u'n：%s 以内素数为：%s， 个数为：%s' %(n, result[1], result[0])
    # print u'耗时：%s' %use_time
    # 