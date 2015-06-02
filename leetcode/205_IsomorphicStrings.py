#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
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
        if not s and not t:
            return True
        elif not s or not t:
            return False
        dic = {}
        dics = 




if __name__ == '__main__':
    sol = Solution()
    

    

    start_time = time.time()
    result = sol.reverseList2(h1)
    use_time = time.time() - start_time
    
    print u'原始链表为：%s, 反转后的链表为：%s' %(str(h1), str(result))
    print u'耗时：%s' %use_time








