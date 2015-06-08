#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Contains Duplicate II
Given an array of integers and an integer k , find out whether 
there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the difference between i and j is at most k

给定一个整数数组 和数字k，找到一个重复的数字，并且数字之间的位置的距离在k以内
"""
class Solution(object):
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearByDuplicate(self, nums, k):
        dic = {}
        for position, value in enumerate(nums):
            dic.setdefault(value,[]).append(position)

        for key in dic:       
            if len(dic[key]) > 1:             
                for i in range(0, len(dic[key])-1):
                    if abs(dic[key][i] - dic[key][i+1]) <= k:               
                        return True
        return False

    def containsNearByDuplicate2(self, nums, k):
        """ use dict """
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                j = d[nums[i]]
                if abs(i - j) <= k:
                    return True
            d[nums[i]] = i
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,4,5,6,5,4,3,2]
    k = 3

    start_time = time.time()
    result = sol.containsNearByDuplicate(nums, k)
    use_time = time.time() - start_time

    print u'nums is : %s, 重复值是否在 %s 的两边： %s' %(nums, k, result)
    print u'耗时：%s' %use_time

