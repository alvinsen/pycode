#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import division
import time
"""
Invert Binary Tree
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

反转二叉树

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        """ 递归解法 """
        if not root:
            return root
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root

    def invertTree2(self, root):
        """ 非递归版本：迭代 """
        if not root:
            return root
        queue = [root]
        while queue:
            front = queue.pop(0)
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
            front.left, front.right = front.right, front.left
        return root

    def invertTree3(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invertTree4(self, root):
        if root:
            invert = self.invertTree
            root.left, root.right = invert(root.right), invert(root.left)
        return root

    def invertTree5(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root

if __name__ == '__main__':
    sol = Solution()
    
    root = TreeNode(4)
    left0 = TreeNode(2)
    right0 = TreeNode(7)
    root.left, root.right = left0, right0

    left0_left = TreeNode(1)
    left0_right = TreeNode(3)
    left0.left, left0.right = left0_left, left0_right

    right0_left = TreeNode(6)
    right0_right = TreeNode(9)
    right0.left, right0.right = right0_left, right0_right

    start_time = time.time()
    result = sol.invertTree(root)
    use_time = time.time() - start_time

    print '-'*40
    print u'二叉树为：%s, 反转后的二叉树为：%s' %(root, result)
    print '耗时：%s' %use_time

    start_time = time.time()
    other_result = sol.invertTree2(result)
    use_time = time.time() - start_time

    print '-'*40
    print u'反转后的二叉树为：%s, 再次反转后的二叉树为：%s' %(result, other_result)
    print '耗时：%s' %use_time

    print '两次反转后的二叉树和原二叉树是否相等：%s' %(root == other_result)

