#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
无向图的最小生成树算法：Prim算法（普里姆）
最小生成树 prim算法的python实现  
普里姆（Prim）算法：由线到点，适合边稠密。时间复杂度O(N^2) 
"""
MAXNUM = 65535
class Graph(object):
    """
        无向图：使用邻接矩阵创建图
        Python的图邻接矩阵法做为存储结构，0表示节点为自己，MAXNUM = 65535表示不可达，其他正数表示边的权值。
    """
    def __init__(self, nodenum = 0):
        self.map = []       #图的矩阵结构
        self.nodenum = self.get_node_num() #节点数

    def init(self):
        """ 初始化方法，每次添加以后，都把节点自己权值置为0 """
        for i in range(self.nodenum):
            self.map[i][i] = 0

    def is_out_range(self, x):
        try :
            if x >= self.nodenum or x <= 0:
                raise IndexError
        except IndexError:
            print u'节点下标出界'

    def get_node_num(self):
        self.nodenum = len(self.map)
        return self.nodenum

    def add_node(self):
        for i in range(self.nodenum):
            self.map[i].append(MAXNUM)
        self.nodenum = self.nodenum + 1
        # 添加顶点时，默认为不可达
        ls = [MAXNUM] * self.nodenum
        self.map.append(ls)
        self.init()

    def delete_node(self, x):
        # 假删除，只是归零而已
        for i in range(self.nodenum):
            if self.map[i][x] > 0:
                self.map[i][x] = MAXNUM
            if self.map[x][i] > 0:
                self.map[x][i] = MAXNUM

    def add_edge(self, x, y, w):
        """ 添加边，x 弧尾，y 弧头，w 边的权值 """
        # 由于是无向图，矩阵对称
        self.map[y][x] = self.map[x][y] = w

    def remove_edge(self, x, y):
        if self.map[x][y] > 0:
            self.map[x][y] = self.map[y][x] = MAXNUM


def MiniSpanTree_Prim(graph):
    """ 
        最小生成树prim 算法
        来自：大话数据结构 P247
        adjvex: 保存相关顶点的下标 [0, 0, 1, 0, 0, 0, 1, 0, 1]  1值表示 下标为2的和1有联系，下标为6的和1有联系，下标为8的和1有联系
            adjvex[i]: 表示 i 和当前树上节点所连的最小边（到目前树上哪个节点最近） adjvex[i]=k 表示i和k 离得最近
        lowcost: 保存相关顶点间边的权值 
    """
    min_tree = []
    g = graph
    nodenum = g.nodenum
    adjvex = [0]    # 从下标为0 开始，作为最小生成树的根开始遍历，权值为0
    lowcost = [0]   # 从下标为0 开始
    # 初始化操作，将第0行 所有权值加入数组，并且adjvex初始化全部为0的下标
    for i in range(1, nodenum):
        lowcost.append(g.map[0][i])
        adjvex.append(0)

    # 正式开始构造最小生成树
    for i in range(1, nodenum):
        # 初始化最小权值为 MAXNUM = 65535
        minv = MAXNUM
        j = 1
        k = 0
        # 遍历全部顶点
        while j < nodenum:
            # 找出lowcost数组已存储的最小权值。如果权值不等于0， 并且不小于minv
            if lowcost[j] != 0 and lowcost[j] < minv:
                minv = lowcost[j]
                k = j  # 将发现的最小权值的下标置为 k
            j += 1

        # 打印当前顶点边中权值最小的边, adjvex[k] 表示上一次找到的最小值的下标
        # print '(%d, %d), weight: %s' %(adjvex[k], k, lowcost[k]) 
        min_tree.append({'(%d, %d)'%(adjvex[k],k): lowcost[k]})
        # 将当前顶点的权值置为0，表示当前顶点已经完成任务
        lowcost[k] = 0 
        # 邻接矩阵 k 行逐个遍历所有顶点， g.map[k][j] 表示k 行所有顶点
        for j in range(1, nodenum):
            # 循环结束以后：[0, 0, 18, 65535, 65535, 11, 16, 65535, 12] 
            if lowcost[j] != 0 and g.map[k][j] < lowcost[j]:
                lowcost[j] = g.map[k][j]
                # j 元素与 k 元素有联系。。。
                adjvex[j] = k

    print min_tree
    return min_tree

if __name__ == '__main__':
    # 邻接矩阵实现图结构
    g = Graph()
    # 生成5个顶点的图
    for i in range(9):
        g.add_node()

    g.add_edge(0, 1, 10)
    g.add_edge(0, 5, 11)
    g.add_edge(1, 2, 18)
    g.add_edge(1, 6, 16)
    g.add_edge(1, 8, 12)
    g.add_edge(2, 3, 22)
    g.add_edge(2, 8, 8)
    g.add_edge(3, 4, 20)
    g.add_edge(3, 7, 16)
    g.add_edge(3, 8, 21)
    g.add_edge(4, 5, 26)
    g.add_edge(4, 7, 7)     
    g.add_edge(5, 6, 17)
    g.add_edge(6, 7, 19)

    # print '初始化创建图形结构: ', g.map
    MiniSpanTree_Prim(g)

