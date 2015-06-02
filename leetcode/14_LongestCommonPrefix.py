#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Write a function to find the longest common prefix string amongst an array of strings.

"""
class Solution(object):
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        prefix_lst = []
        for z in zip(*strs):
            ba = set(z)
            if len(ba) == 1:
                prefix_lst.append(ba.pop())
            else:
                break
        return ''.join(prefix_lst)

    def longestCommonPrefix2(self, strs):
        if not strs:
            return ''
        first_str = strs[0]
        res = ''
        for i in range(len(first_str)):
            for j in range(1,len(strs)):
                if i > len(strs[j]) - 1:
                    return res
                if first_str[i] != strs[j][i]:
                    return res
            res += first_str[i]
        return res

    def longestCommonPrefix3(self, strs):
        def getLCP(x,y):    
            n, lcp = min(len(x), len(y)), ''
            for i in range(n):
                if x[i] != y[i]:
                    break
                else:
                    lcp += x[i]
            return lcp

        if not strs:
            return ''
        return reduce(getLCP, strs)


if __name__ == '__main__':
    sol = Solution()
    strs = ['abc','abb','acdb']
    correct = 'a'

    start_time = time.time()
    result = sol.longestCommonPrefix(strs)
    use_time = time.time() - start_time

    print '-'*40
    print u'数组：%s, 最长的前缀是：%s' %(strs, result)
    print '耗时：%s' %use_time

    start_time = time.time()
    result = sol.longestCommonPrefix2(strs)
    use_time = time.time() - start_time

    print '-'*40
    print u'数组：%s, 最长的前缀是：%s' %(strs, result)
    print '耗时：%s' %use_time

    start_time = time.time()
    result = sol.longestCommonPrefix3(strs)
    use_time = time.time() - start_time

    print '-'*40
    print u'数组：%s, 最长的前缀是：%s' %(strs, result)
    print '耗时：%s' %use_time
