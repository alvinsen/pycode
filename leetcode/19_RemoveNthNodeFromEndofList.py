#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
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
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def removeNthFromEnd2(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]

    def removeNthFromEnd3(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next
        
    def removeNthFromEnd4(self, head, n):
        if head.next==None:
            return None
        Node = head
        flag = n
        while True:
            myNode = Node
            while n > 1:
                myNode = myNode.next
                n -= 1
            if myNode.next == None:
                head = head.next
                return head
            if myNode.next.next == None:
                break
            Node = Node.next
            n = flag
        Node.next = Node.next.next
        return head

    def removeNthFromEnd5(self, head, n):
        dummyHead = ListNode(0)
        dummyHead.next = head
        slow = fast = dummyHead

        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummyHead.next

if __name__ == '__main__':
    sol = Solution()
    
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5

    n = 2

    start_time = time.time()
    print u'原始链表为：%s ' %(str(h1))
    result = sol.removeNthFromEnd(h1, n)
    use_time = time.time() - start_time
    
    print u'从后开始删除第 %s 个元素后的链表为：%s' %(n, str(result))
    print u'耗时：%s' %use_time


