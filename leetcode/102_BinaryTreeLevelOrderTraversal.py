#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
"""
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
confused what "{1,#,2,3}" means? 
    1
   / \
  4   2
  \   / 
   5 3   

OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        """ 先进先出的理念 """
        levels, result = [[root]], []
        while levels:
            curLevel = levels.pop()
            newLevel, curValues = [], []
            for node in curLevel:
                if node:
                    newLevel += [node.left, node.right]
                    curValues.append(node.val)
            if newLevel:
                levels.append(newLevel)
            if curValues:
                result.append(curValues)
        return result

    def levelOrder2(self, root):
        """ 树 """
        result = []
        if not root:
            return result
        curlevel = [root]
        while curlevel != []:
            vals = []
            newlevel = []
            for node in curlevel:
                vals.append(node.val)
                if node.left:
                    newlevel.append(node.left)
                if node.right:
                    newlevel.append(node.right)
            result.append(vals)
            curlevel = newlevel
        return result


if __name__ == '__main__':
    sol = Solution()
    [1,'#',3,4,5]
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3)
    n3.left,n3.right = n4,n5

    n1 = TreeNode(1)
    n1.right = n3

    start_time = time.time()
    result = sol.levelOrder(n1)
    use_time = time.time() - start_time

    print '-'*40
    print u'二叉树结构：%s' %(result)
    print '耗时：%s' %use_time


    start_time = time.time()
    result = sol.levelOrder2(n1)
    use_time = time.time() - start_time

    print '-'*40
    print u'二叉树结构：%s' %(result)
    print '耗时：%s' %use_time

