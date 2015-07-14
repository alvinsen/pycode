#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
"""
无向图的最短路径算法：Floyd算法（弗洛伊德）
最短路径 floyd算法的python实现  
弗洛伊德（Floyd）算法。
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


def ShortestPathTree_Floyd(graph):
    """ 
    最短路径树floyd 算法
    
    @return 返回每一个顶点到源点的最短路径
    """
    g = graph
    n = g.nodenum

    edges = copy.deepcopy(g.map)
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                if edges[i][j] > edges[i][k] + edges[k][j]:
                    edges[i][j] = edges[i][k] + edges[k][j]

    print "最短路径为：%s" %edges

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

    print '初始化创建图形结构: ', g.map
    ShortestPathTree_Floyd(g)
