#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import timeit
"""
Contains Duplicate
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

"""
class Solution(object):
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        nums_set = set(list(nums))
        if len(nums_set) < len(nums):
            return True
        return False

    def containsDuplicate2(self, nums):
        dic = {}
        for num in nums:
            res = dic.get(num, None)
            if res is not None:
                return True
            dic[num] = 1
        return False

    def containsDuplicate3(self, nums):
        return not (len(nums) == len(set(nums))) 

    def containsDuplicate4(self, nums):
        return len(nums) > len(set(nums))

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,1]

    start_time = time.time()
    result = sol.containsDuplicate(nums)
    use_time = time.time() - start_time

    print 'nums is : %s, 是否有重复值： %s' %(nums, result)
    print '耗时：%s' %use_time

    start_time = time.time()
    result = sol.containsDuplicate2(nums)
    use_time = time.time() - start_time

    print 'nums is : %s, 是否有重复值： %s' %(nums, result)
    print '耗时：%s' %use_time

    start_time = time.time()
    result = sol.containsDuplicate3(nums)
    use_time = time.time() - start_time

    print 'nums is : %s, 是否有重复值： %s' %(nums, result)
    print '耗时：%s' %use_time

    start_time = time.time()
    result = sol.containsDuplicate4(nums)
    use_time = time.time() - start_time

    print 'nums is : %s, 是否有重复值： %s' %(nums, result)
    print '耗时：%s' %use_time

    
