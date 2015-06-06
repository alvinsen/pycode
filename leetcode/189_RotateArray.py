#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Rotate Array

Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
[1,2], k=1 ---> [2,1]
Note:
Try to come up as many solutions as you can, there are at least 3 different ways 
to solve this problem.

"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if len(nums) < k:
            return nums
        nums[:] = nums[len(nums)-k:] + nums[:len(nums) - k]
        return nums

    def rotate2(self, nums, k):
        nums[k % len(nums):], nums[:k % len(nums)] = nums[:len(nums)-k % len(nums)], nums[len(nums)-k % len(nums):]
        return nums

    def rotate3(self, nums, k):
        k = -k
        return nums[k:] + nums[:k]

    def rotate4(self, nums, k):
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        return nums

if __name__ == '__main__':
    sol = Solution()

    nums = [1,2,3,4,5,6,7]
    #nums = [1,2]
    k = 3
    #k = 1
    
    start_time = time.time()
    result = sol.rotate(nums, k)
    use_time = time.time() - start_time

    print '-'*20 + 'Rotate Array' + '-'*20
    print u'nums：%s，从 %s 位, 反转后为：%s ' %(nums, k, result)
    print u'耗时：%s' %use_time

    # start_time = time.time()
    # result = sol.rotate2(nums, k)
    # use_time = time.time() - start_time

    # print '-'*20 + 'Rotate Array' + '-'*20
    # print u'nums：%s，从 %s 位, 反转后为：%s ' %(nums, k, result)
    # print u'耗时：%s' %use_time

    # start_time = time.time()
    # result = sol.rotate3(nums, k)
    # use_time = time.time() - start_time

    # print '-'*20 + 'Rotate Array' + '-'*20
    # print u'nums：%s，从 %s 位, 反转后为：%s ' %(nums, k, result)
    # print u'耗时：%s' %use_time

