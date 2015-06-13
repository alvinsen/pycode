#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

看看两个链表相交到底是怎么回事吧，有这样的的几个事实：（假设链表中不存在环）
　　（1）一旦两个链表相交，那么两个链表中的节点一定有相同地址。
　　（2）一旦两个链表相交，那么两个链表从相交节点开始到尾节点一定都是相同的节点。
　　分析出来了问题的本质，那么思路也就自然有了。

思路：
1、碰到这个问题，第一印象是采用hash来判断，将两个链表的节点进行hash，然后判断出节点，这种想法当然是可以的。
2、当然采用暴力的方法也是可以的，遍历两个链表，在遍历的过程中进行比较，看节点是否相同。
3、第三种思路是比较奇特的，在编程之美上看到的。先遍历第一个链表到他的尾部，
然后将尾部的next指针指向第二个链表(尾部指针的next本来指向的是null)。
这样两个链表就合成了一个链表，判断原来的两个链表是否相交也就转变成了判断新的链表是否有环的问题了：
即判断单链表是否有环？

4、仔细研究两个链表，如果他们相交的话，那么他们最后的一个节点一定是相同的，否则是不相交的。
因此判断两个链表是否相交就很简单了，分别遍历到两个链表的尾部，然后判断他们是否相同，如果相同，则相交；否则不相交。


算法思想：
用两个指针p1,p2同时指向链表的头部，p1一次移动一步，p2一次移动两步，如果最终p1和p2重合则说明链表有环，
如果p2走到空指针（链表的结尾）则说明链表无环； 
如果最终p1和p2重合，使p2重新指向链表的头结点，然后p1和p2同时一次移动一步，
当p1和p2再次重合时该节点指针就是环的入口节点指针。

/*判断链表是否有环，如果有环则返回环的首结点指针，否则返回NULL值*/    
Node* findCircle(Node *head)    
{    
    if(head==NULL)    
        return NULL;    
    Node *p1=head;    
    Node *p2=head;    
    /*判断链表是否有环，当p1=p2时说明链表有环，程序跳出循环。如果p2一直走到链表尽头则说明没有环。*/    
    do{    
        if(p1->next!=NULL&&p2->next!=NULL&&p2->next->next!=NULL)    
        {    
            p1=p1->next;    
            p2=p2->next->next;       
        }    
        else    
            return NULL;    
    }    
    while(p1!=p2);    
        
    /*求出环的起点节点，并将其返回*/    
    p2=head;    
    while(p1!=p2)    
    {    
        p1=p1->next;    
        p2=p2->next;        
    }    
    return p1;           
}

struct Node    
{    
    int value;    
    Node *next;        
};    
/*判断两个链表是否交叉，如果交叉返回交叉节点，否则返回NULL。*/    
Node* findCross(Node* head1,Node* head2)    
{    
    if(head1==NULL||head2==NULL)    
        return NULL;    
    /*将第二个链表变成有环链表*/    
    Node* tail2=head2;    
    while(tail2->next!=NULL)    
        tail2=tail2->next;    
    tail2->next = head2;    
           
    Node* temp = findCircle(head1);    
    if(temp!=NULL)    
        return temp;    
    else    
        return NULL;    
              
}

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

    # def __str__(self):
    #     result = []
    #     while True:
    #         result.append(str(self.val))
    #         if self.next == None:
    #             break
    #         self = self.next
    #     result_str = ' -> '.join(result)
    #     return result_str

    # __repr__ = __str__

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        def findCircle(head):
            head1 = head2 = head
            while True:
                ### 判断是否有环，指针1 走一步，指针2 走两步，如果有环，则指正1 == 指正2
                if head1.next and head2.next and head2.next.next:
                    head1 = head1.next
                    head2 = head2.next.next
                else:    
                    return None   
                if head1 == head2:
                    break
            ### 指正2 走了两步以后，确定有环，此时开始走一步，指正1继续走一步。如果指正1 == 指正2，则相交
            head2 = head
            while True:
                head1 = head1.next
                head2 = head2.next
                if head1 == head2:
                    break
            return head1

        # 将第二个链表接在第一个链表后面，然后判断第一个链表是否有环        
        head1 = headA
        head2 = headB

        tail1 = head1
        while tail1.next:    
            tail1 = tail1.next  
        tail1.next = head2  

        return findCircle(head1)


if __name__ == '__main__':
    sol = Solution()
    
    a1 = ListNode(11)
    a2 = ListNode(12)
    c1 = ListNode(31)
    c2 = ListNode(32)
    c3 = ListNode(33)        

    b1 = ListNode(21)    
    b2 = ListNode(22)
    b3 = ListNode(23)

    a1.next = a2
    a2.next = c1
    c1.next = c2
    c2.next = c3

    b1.next = b2
    b2.next = b3
    b3.next = c1

    start_time = time.time()
    result = sol.getIntersectionNode(a1, a2)
    use_time = time.time() - start_time

    print '-'*20 + ' Intersection of Two Linked Lists ' + '-'*20
    print u'链表A：%s, 链表B：%s, 相交的点为：%s ' %(a1, a2, result)
    print u'耗时：%s' %use_time

