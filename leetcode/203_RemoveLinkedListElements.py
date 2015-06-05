#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import copy
"""
Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __len__(self):
    #     size = 0
    #     while True:
    #         size += 1
    #         if self.next == None:
    #             break
    #         self = self.next
    #     return size

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
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        first = temp = ListNode(0)
        while head:
            head_val = head.val
            head = head.next
            if head_val == val:
                continue

            temp.next = ListNode(head_val)
            temp = temp.next

        return first.next

    def removeElements2(self, head, val):
        """ 递归调用，在层数多的时候，会造成性能问题 """
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

    def removeElements3(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head:
            if head.val == val:
                prev.next = head.next
                head = prev
            prev = head
            head = head.next
        return dummy.next

    def removeElements4(self, head, val):
        """ 两个链表，一个表示prev， 一个表示curr """
        handle = ListNode(-1)
        handle.next = head
        prev, curr = handle, handle.next
        while curr:
            if curr.val==val:
                prev.next = curr.next
                curr = curr.next
                continue
            prev, curr = prev.next, curr.next
        return handle.next


if __name__ == '__main__':
    sol = Solution()
    head = temp = ListNode(0)
    n = 1
    while n < 100:
        temp.next = ListNode(n)
        temp = temp.next
        n += 1

    source1 = copy.deepcopy(head)
    source2 = copy.deepcopy(head)
    source3 = copy.deepcopy(head)

    # 被移除的元素
    val = 1
    start_time = time.time()
    result = sol.removeElements(source1, val)
    use_time = time.time() - start_time

    print '-'*40
    # print u'链表为：%s，移除元素：%s，后链表为：%s' %(head, val, result)
    print u'耗时：%s' %use_time

    start_time = time.time()
    result = sol.removeElements2(source2, val)
    use_time = time.time() - start_time

    print '-'*40
    # print u'链表为：%s，移除元素：%s，后链表为：%s' %(head, val, result)
    print u'耗时：%s' %use_time

    start_time = time.time()
    result = sol.removeElements3(source3, val)
    use_time = time.time() - start_time

    print '-'*40
    # print u'链表为：%s，移除元素：%s，后链表为：%s' %(head, val, result)
    print u'耗时：%s' %use_time

