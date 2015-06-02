#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Add Two Numbers
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
给你两个链表代表两个非负数。数字以相反的顺序存储，每个节点包含一个单一的数字。加上这两个数并返回一个链表。

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Tags: Linked List Math
"""

# Definition for singly-linked list.
class ListNode(object):
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


class Solution(object):
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers1(self, l1, l2):
        """ 错误。理解错题意 """
        size = len(l1) if len(l1) > len(l2) else len(l2)
        result_list = []
        for index in xrange(size):
            val = l1.val + l2.val
            l1 = l1.next if l1.next is not None else ListNode(0)
            l2 = l2.next if l2.next is not None else ListNode(0)
            result_list.append(val)

        result = None
        while result_list:
            temp_next = result
            result = ListNode(result_list.pop())
            result.next = temp_next

        return result

    def addTwoNumbers2(self, l1, l2):
        """ 错误。理解错题意 """
        result_list = []
        need_break = False
        while True:
            val = l1.val + l2.val
            if l1.next is None and l2.next is None:
                need_break = True

            l1 = l1.next if l1.next is not None else ListNode(0)
            l2 = l2.next if l2.next is not None else ListNode(0)
            result_list.append(val)
            if need_break:
                break
        result = None
        while result_list:
            temp_next = result
            result = ListNode(result_list.pop())
            result.next = temp_next

        return result


    def addTwoNumbers_modify(self, l1, l2):
        """ 正确答案，需要提高效率 """
        result_list = []
        need_break = False
        back_add = 0
        while True:
            val = l1.val + l2.val + back_add
            if l1.next is None and l2.next is None:
                need_break = True

            l1 = l1.next if l1.next is not None else ListNode(0)
            l2 = l2.next if l2.next is not None else ListNode(0)

            if val > 9:
                back_add = val / 10
                val = val % 10

            result_list.append(val)
            bak_add = 0
            if need_break:
                break
        result = None
        while result_list:
            temp_next = result
            result = ListNode(result_list.pop())
            result.next = temp_next
        return result

    def addTwoNumbers_modify_beta(self, l1, l2):
        """ 正确答案， 修改版 """
        def toint(node):
            """ ListNode 转 int """
            return node.val + 10 * toint(node.next) if node else 0

        total = toint(l1) + toint(l2)
        first = last = ListNode(total % 10)
        while total > 9:
            total = total / 10
            last.next = last = ListNode(total % 10)
        """
        什么梗啊，啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
        """
        return last

    def addTwoNumbers_modify_beta2(self, l1, l2):
        """ 正确答案， 修改版 """
        def toint(node):
            """ ListNode 转 int """
            return node.val + 10 * toint(node.next) if node else 0
        def int2list(n):
            """ 4110 -> [0,1,1,4] """
            result = []
            result.append(n % 10)
            while n > 9:
                n = n / 10
                result.append(n % 10)
            return result

        result_list = int2list(toint(l1) + toint(l2))
        result = None
        while result_list:
            temp_next = result
            result = ListNode(result_list.pop())
            result.next = temp_next
        return result


    def addTwoNumbers3(self, l1, l2):
        """ 正确答案 """
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node
        return tolist(toint(l1) + toint(l2))


    def addTwoNumbers4(self, l1, l2):
        """ 正确答案2 """
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        n = toint(l1) + toint(l2)
        first = last = ListNode(n % 10)
        while n > 9:
            n /= 10
            last.next = last = ListNode(n % 10)
        return first

    def addTwoNumbers5(self, l1, l2):
        """ 正确答案3 """
        head = temp = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            tempSum = temp1 + temp2 + carry

            temp.next = ListNode(tempSum % 10)
            temp = temp.next
            carry = tempSum // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next


if __name__ == '__main__':

    
    l1 = ListNode(5)

    l2 = ListNode(5)
        
    print 'l1 :%s, l2: %s' %(l1, l2)

    sol = Solution()
    l3 = sol.addTwoNumbers3(l1, l2)
    print l3

    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)

    print l1

    l2 = ListNode(10)
    l2.next = ListNode(9)
    l2.next.next = ListNode(8)

    print l2

    l3 = sol.addTwoNumbers4(l1, l2)
    print l3

    l5 = sol.addTwoNumbers_modify(l1, l2)
    print l5

    l6 = sol.addTwoNumbers_modify_beta2(l1, l2)
    print 'l6: %s' %l6

    l7 = sol.addTwoNumbers5(l1,l2)
    print 'l7: %s' %l7
    
