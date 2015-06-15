#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Merge Two Sorted Lists 
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
这道题主要是用到了归并排序的思想：
维护两个指针对应两个链表，因为一般会以一条链表为基准，比如说l1, 那么如果l1当前的元素比较小，那么直接移动l1即可，
否则将l2当前的元素插入到l1当前元素的前面。
算法时间复杂度是O(m+n),m和n分别是两条链表的长度，空间复杂度是O(1)，代码如下：

这个题类似的有Merge Sorted Array： 对数组进行合并操作。
扩展题目Merge k Sorted Lists, 这是一个在分布式系统中比较有用的基本操作。

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __len__(self):
        size = 0
        while True:
            size += 1
            if self.next == None:
                break
            self = self.next
        return size

    def __str__(self):
        result = []
        while True:
            result.append(str(self.val))
            if self.next == None:
                break
            self = self.next
        result_str = ' -> '.join(result)
        return result_str

    __repr__ = __str__

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        # 合并两个链表
        last = dummy = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val > l2.val:
                node = l2.next
                l2.next = last.next
                last.next = l2
                l2 = node
            else:
                l1 = l1.next
            last = last.next
        if l2:
            last.next = l2
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    
    l1 = ListNode(1)
    l2 = ListNode(2)
    
    l1_1 = ListNode(3)
    l1_2 = ListNode(5)
    l1_3 = ListNode(9)    
    l1.next = l1_1
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(4)
    l2_2 = ListNode(6)
    l2_3 = ListNode(8)
    l2.next = l2_1
    l2_1.next = l2_2
    l2_2.next = l2_3

    start_time = time.time()
    print u'原始链表为l1：%s, l2: %s,' % (l1, l2)
    result = sol.mergeTwoLists(l1, l2)
    use_time = time.time() - start_time
    
    print u'合并后的链表为：%s' %(str(result))
    print u'耗时：%s' %use_time

