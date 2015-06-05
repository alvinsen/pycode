#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
House Robber
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

求数组中，不相邻的数的最大和
"""
# Definition for singly-linked list.
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        left = left_left = 0
        for i in xrange(len(nums)):
            print 'nums[%s]: %s, left_left:%s, left: %s' %(i, nums[i], left_left, left) 
            left, left_left =  max(nums[i] + left_left, left), left
        return left

    def rob2(self, nums):
        if len(nums)==0:
            return 0
        r = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                r[0] = nums[0]
            elif i == 1:
                r[1] = max(nums[0], nums[1])
            else:
                r[i] = max(r[i-1], r[i-2] + nums[i])

        return r[-1]


if __name__ == '__main__':
    sol = Solution()

    nums = [18, 35, 44, 22, 10, 9, 45]

    start_time = time.time()
    result = sol.rob(nums)
    use_time = time.time() - start_time

    print '-'*20 + 'House Robber' + '-'*20
    print u'序列为：%s，间隔最大的数：%s ' %(nums, result)
    print u'耗时：%s' %use_time


    start_time = time.time()
    result = sol.rob2(nums)
    use_time = time.time() - start_time

    print '-'*20 + 'House Robber' + '-'*20
    print u'序列为：%s，间隔最大的数：%s ' %(nums, result)
    print u'耗时：%s' %use_time
