#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import division
import time
"""
Rectangle Area
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

思路：判断两个矩形是否相交
简单计算集合。根据容斥原理：S(M ∪ N) = S(M) + S(N) - S(M ∩ N)
题目可以转化为计算矩形相交部分的面积

S(M) = (C - A) * (D - B)
S(N) = (G - E) * (H - F)
S(M ∩ N) = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)

"""
# Definition for a binary tree node.
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
            矩形1（左下点：AB, 右上点：CD），矩形2（左下点：EF，右上点：GH）
            总面积 = 1的面积 + 2的面积 - 重合的面积
        """
        sums = (C - A) * (D - B) + (G - E) * (H - F)
        return sums - max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)

if __name__ == '__main__':
    sol = Solution()
    
    A, B = (-3, 0)
    C, D = (3, 4)
    E, F = (0, -1)
    G, H = (9, 2)

    ### 0, 0, 0, 0, -1, -1, 1, 1
    A, B = (0, 0)
    C, D = (0, 0)
    E, F = (-1, -1)
    G, H = (1, 1)

    start_time = time.time()
    result = sol.computeArea(A,B,C,D,E,F,G,H)
    use_time = time.time() - start_time

    print '-'*40
    print u'矩形1为：[({A}, {B}),({C},{D}))], 矩形2为：[({E}, {F}),({G},{H}))]。矩形的面积为：{area}'.format(A=A,B=B,C=C,D=D,E=E,F=F,G=G,H=H,area=result)
    print '耗时：%s' %use_time



