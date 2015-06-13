#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Compare Version Numbers
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", 
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

"""
class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        """
            此种解法，主要使用了 zip() ,itertools.izip(), itertools.izip_longest()
            zip(): 将两个序列的对应位置的元素，组合成元组，返回元组的最短序列
            itertools.izip(): 类似于zip()，不过返回的是一个迭代器
            itertools.izip_longest(): 类似于izip，不过返回的是最长序列，支持fillvalue来填充短序列的值
        """
        import itertools

        version1 = map(int, version1.split('.'))
        version2 = map(int, version2.split('.'))
        for i, j in itertools.izip_longest(version1, version2, fillvalue=0):
            i, j = int(i), int(j)
            if i < j:
                return -1
            if i > j:
                return 1
        return 0

    def compareVersion2(self, version1, version2):
        """ 数组长度一样时在进行比较 """
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) < len(v2):
            for i in range(len(v2) - len(v1)):
                v1.append('0')
        if len(v1) > len(v2):
            for i in range(len(v1) - len(v2)):
                v2.append('0')
        for i in range(len(v1)):
            j, k = int(v1[i]), int(v2[i])
            if j < k:
                return -1
            if j > k:
                return 1
        return 0

if __name__ == '__main__':
    sol = Solution()
    
    version1 = '1.5.6'
    version2 = '1.10'

    start_time = time.time()
    result = sol.compareVersion2(version1, version2)
    use_time = time.time() - start_time

    print '-'*20 + ' Compare Version Numbers ' + '-'*20
    print u'版本1：%s, 版本2：%s, 版本比较哪个大（1：前一个大，-1：后一个大，0：一样大）：%s ' %(version1, version2, result)
    print u'耗时：%s' %use_time

