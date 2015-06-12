#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Majority Element
Given an array of size n, find the majority element. The majority element is the element that 
appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority 
element always exist in the array.

"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        n = len(nums)
        dic = {}
        for position, value in enumerate(nums):
            dic.setdefault(value,[]).append(position)

        lst = sorted(dic.iteritems(), key=lambda d: len(d[1]), reverse=True)
        for key, val in lst:
            if len(val) >= n/2:
                return key
        return 0

    def majorityElement2(self, nums):
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
            if count[i] > len(nums)/2:
                return i

    def majorityElement3(self, nums):
        myset = list(set(nums))
        # get a comma separated list of all members in num

        for i in myset:
            c = [val for val in sorted(nums) if val == i]
            # count the occurences of a list member within the array
            if len(c) > (len(nums)/2):
                # run the majority check (appears more than n/2 times)
                print "majority element is:", i
                return i
                break

    def majorityElement4(self, nums):
        return sorted(nums)[len(nums)/2]


if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,4,5,9,3,3,3,3,3]
    
    start_time = time.time()
    result = sol.majorityElement4(nums)
    use_time = time.time() - start_time

    print '-'*20 + 'Rotate Array' + '-'*20
    print u'数组为：%s，数组中魔法数字(出现次数大于等于n/2)是：%s ' %(nums, result)
    print u'耗时：%s' %use_time

