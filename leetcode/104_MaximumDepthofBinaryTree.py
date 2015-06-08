#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        count = 0
        levels = [[root]]
        while levels:
            curLevel = levels.pop()
            newLevel = []
            for node in curLevel:
                if node:
                    newLevel += [node.left, node.right]
            if newLevel:
                levels.append(newLevel)
                count += 1
        return count 


    def maxDepth2(self, root):
        """ 递归二叉树 """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == '__main__':
    sol = Solution()
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3)
    n3.left,n3.right = n4,n5

    n1 = TreeNode(1)
    n1.right = n3

    start_time = time.time()
    result = sol.maxDepth2(n1)
    use_time = time.time() - start_time

    print '-'*40
    print u'二叉树的深度为：%s' %(result)
    print '耗时：%s' %use_time



