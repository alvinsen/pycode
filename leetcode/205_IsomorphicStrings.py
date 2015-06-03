
#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Isomorphic Strings 
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ###part1:substituting s with t
        d = {}
        for i in range(len(s)):
            d[s[i]] = t[i]
        tempS1 = list(s[:])
        tempT1 = list(t[:])
        for i in range(len(s)):
            tempS1[i] = d[tempS1[i]]
        if tempS1 != tempT1:
            return False

        ###part2:substituting t with s
        d = {}
        for i in range(len(s)):
            d[t[i]] = s[i]
        tempS2 = list(s[:])
        tempT2 = list(t[:])
        for i in range(len(s)):
            tempT2[i] = d[tempT2[i]]
        if tempS2 != tempT2:
            return False

        return True

    def isIsomorphic2(self, s, t):
        """ 第二种方式, 牛 """
        """ 
            python 中 字典的setdefault() 方法，如果有值，
        """
        return all(map({}.setdefault, a, b) == list(b) for a, b in ((s, t), (t, s)))


if __name__ == '__main__':
    sol = Solution()
    
    s1 = 'foo'
    t1 = 'bar'

    s2 = 'egg'
    t2 = 'add'

    s3 = 'paper'
    t3 = 'title'

    s4 = 'ac'
    t4 = 'ab'

    s5 = 'a'
    t5 = 'a'

    s6 = 'ab'
    t6 = 'ca'

    lst = [(s1, t1), (s2, t2), (s3, t3), (s4, t4), (s5, t5), (s6, t6)]

    for tup in lst:
        start_time = time.time()
        result = sol.isIsomorphic(tup[0], tup[1])
        use_time = time.time() - start_time
        
        print u'字符串1为：%s, 字符串2为：%s, 是否同构字符串：%s' %(tup[0], tup[1], result)
        print u'耗时：%s' %use_time

