#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid 
but "(]" and "([)]" are not.

"""
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        dic = {')':'(', ']':'[', '}':'{'}
        stack = [' ']
        for i in s:
            if i in '([{':
                stack.append(i)
            elif dic.get(i, None) and dic.get(i, None) != stack.pop():
                return False
        return stack == [' ']

    def isValid2(self, s):
        stack = [' ']
        for c in s:
            if c in '([{':
                stack += c,
            elif ord(c) % ord(stack.pop()) > 2:
                return False
        return stack == [' ']

    def isValid3(self, s):


if __name__ == '__main__':
    sol = Solution()
    
    s = "([)]{}"
    
    start_time = time.time()
    result = sol.isValid(s)
    use_time = time.time() - start_time
    
    print u'原始字符串为： %s 括号是否匹配：%s' %(s, result)
    print u'耗时：%s' %use_time

