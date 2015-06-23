#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
import Queue
"""
    python 二叉树结构
    功能：把一个数组的值存入二叉树中，然后进行3种方式的遍历 
"""
class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):

    def __init__(self):
        self.root = None

    def makeTree(self, data, left, right):  
        self.root = TreeNode(data, left, right) 
        #left.root = right.root = None

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def preOrder(self, treenode):
        """ 先序遍历 """
        if treenode is not None:
            print treenode.data
            if treenode.left is not None:
                self.preOrder(treenode.left)

            if treenode.right is not None:
                self.preOrder(treenode.right)

    def inOrder(self, treenode):
        """ 中序遍历 """
        if treenode is not None:
            if treenode.left is not None:
                self.inOrder(treenode.left)

            print treenode.data
            
            if treenode.right is not None:
                self.inOrder(treenode.right)

    def postOrder(self, treenode):
        """ 后序遍历 """
        if treenode is not None:
            if treenode.left is not None:
                self.preOrder(treenode.left)

            if treenode.right is not None:
                self.preOrder(treenode.right)

            print treenode.data

    def levelOrder(self, a):
        """ 层级遍历 """
        queue = Queue.Queue()
        node = a
        while node is not None:
            print node.data
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
            if queue.empty():
                print "empty"
                node = None
            else:
                node = queue.get()

if __name__ == '__main__':

    """ 创建一个二叉树 """
    # 序列
    lst = random.sample(xrange(100), 10)
    nodelist = []
    # 将序列的值 依次转化为 TreeNode 节点
    for val in lst:
        node = TreeNode(val)
        nodelist.append(node)

    ### level 层数
    # 2**0 + 2**1 + ... + 2**(level-1) = 2**level - 1 = len(nodelist)
    for node in nodelist:
        pass


