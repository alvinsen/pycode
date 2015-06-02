#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        lst = s.strip(' ').split(" ")
        return len(lst[-1])

    def lengthOfLastWord2(self, s):
        """ 第二种方法 """
        return len(s.strip().split(" ")[-1]);

    def lengthOfLastWord3(self, s):
        """ 第三种方法 """
        length, i = 0, len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                if not length:
                    pass
                else:
                    break
            else:
                length += 1
            i -= 1

        return length

    def lengthOfLastWord4(self, s):
        """ 第四种方法 """
        cnt=0
        ### 字符串反转也可以使用另一种方式
        """
        t = list(s)
        t.reverse()
        s = ''.join(t)
        """
        s = s[::-1] 
        for cha in s.strip():
            cnt += 1
            if cha == ' ':
                cnt=0
        return cnt
    

if __name__ == '__main__':
    sol = Solution()
    
    s = 'hello world'
    s = 'a '

    start_time = time.time()
    result = sol.lengthOfLastWord(s)
    use_time = time.time() - start_time

    print u'字符串为：%s, 最后一个单词的长度为：%d' %(s, result)
    print u'耗时：%s' %use_time

    start_time = time.time()
    result = sol.lengthOfLastWord4(s)
    use_time = time.time() - start_time

    print u'字符串为：%s, 最后一个单词的长度为：%d' %(s, result)
    print u'耗时：%s' %use_time
    
    
