#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Reverse a singly linked list.
Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
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
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head): 
        if head is None:
            return None
        #### node-to-list
        nodelist = []
        while True:
            temp = head.next
            head.next = None
            nodelist.append(head)
            head = temp
            if temp == None:
                break

        #### list-to-node
        node = result = ListNode(0)
        for tempnode in nodelist[::-1]:
            # [node1, node2, node3]
            node.next = tempnode
            node = node.next

        return result.next

    def reverseList2(self, head): 
        """ 第二种方式 """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


if __name__ == '__main__':
    sol = Solution()
    
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h1.next = h2
    h2.next = h3
    h3.next = h4

    start_time = time.time()
    result = sol.reverseList2(h1)
    use_time = time.time() - start_time
    
    print u'原始链表为：%s, 反转后的链表为：%s' %(str(h1), str(result))
    print u'耗时：%s' %use_time




