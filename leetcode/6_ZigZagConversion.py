#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


"""
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, nRows):
        """ Error Answer """
        len_s = len(s)
        l = list(s)
        ll = []
        if len_s == 0 or len_s < nRows or nRows == 1:
            return s

        for r in range(0,nRows):
            if r == 0 or r == (nRows - 1):
                gap = 2 * (nRows - 1)
                k = r      
                while k < len_s:
                    ll.append(s[k])
                    k += gap

                else:
                    gap1 = 2 * (nRows - 1)
                    gap2 =2 * (nRows - 1 - r)
                    k = r
                    ll.append(s[k])
                    while k < len_s and gap2 > 0 and (k + gap2) < len_s:
                        ll.append(s[k + gap2])
                        if (k + gap1) < len_s:
                            ll.append(s[k + gap1])
                        k += gap1

        return ''.join(ll)

    def convert(self, s, nRows):
        """ Error Answer """
        len_s = len(s)
        l = list(s)
        ll = []
        if len_s == 0 or len_s < nRows or nRows == 1:
            return s

        for r in range(0,nRows):
            if r == 0 or r == (nRows - 1):
                gap = 2 * (nRows - 1)
                k = r      
                while k < len_s:
                    ll.append(s[k])
                    k += gap

                else:
                    gap1 = 2 * (nRows - 1)
                    gap2 =2 * (nRows - 1 - r)
                    k = r
                    ll.append(s[k])
                    while k < len_s and gap2 > 0 and (k + gap2) < len_s:
                        ll.append(s[k + gap2])
                        if (k + gap1) < len_s:
                            ll.append(s[k + gap1])
                        k += gap1

        return ''.join(ll)


if __name__ == '__main__':
    sol = Solution()

    st = 'PAYPALISHIRING'   # result：PAHNPAAHHNNYIRY
    n = 3
    
    # 此时， convert() 方法是错误的，结果是 ”AABB“， 正确答案是 ”AB“
    st = 'AB'
    n = 2

    start_time = time.time()
    result = sol.convert(st, n)
    use_time = time.time() - start_time

    print '-'*20 + 'ZigZag Conversion' + '-'*20
    print u'source：%s，rows: %s , result：%s ' %(st, n, result)
    print u'耗时：%s' %use_time

    