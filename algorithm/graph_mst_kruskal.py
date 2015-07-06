#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
无向图的最小生成树算法：Kruskal算法（克鲁斯卡尔）
最小生成树 kruskal算法的python实现
图的存贮结构采用边集数组,且权值相等的边在数组中排列次序可以是任意的. 该方法对于边相对比较多的不是很实用,浪费时间.
克鲁斯卡尔（Kruskal）算法。时间复杂度O(n^2) 
"""
MAXNUM = 65535
class Graph(object):
    """
        无向图：使用邻接矩阵创建图, 通过方法 convert_edges 转换为边集数组
        edges = [(weight, (begin, end))]
        weight: 权重
        begin: 起始点
        end: 结束点
    """
    def __init__(self, nodenum = 0):
        self.map = []       # 图的矩阵结构
        self.edges = []     # 图的边集数组结构
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
        # 每次都调用一下 边集数组转换函数
        self.convert_edges()

    def remove_edge(self, x, y):
        if self.map[x][y] > 0:
            self.map[x][y] = self.map[y][x] = MAXNUM

    def convert_edges(self):
        """
        Graph 由邻接矩阵转换为 边集数组
        由于是无向图，所以map[i][j] = map[j][i]
        """
        edges = []
        nodenum = self.nodenum
        for i in range(nodenum):
            for j in range(nodenum):
                if self.map[i][j] != 0 and self.map[i][j] != MAXNUM:
                    edge_weight = (self.map[i][j], (i, j))
                    edge_weight_symmetry = (self.map[i][j], (j, i))
                    if not edge_weight_symmetry in edges:
                        edges.append(edge_weight)
        self.edges = edges

def MiniSpanTree_Kruskal(graph):
    """
    最小生成树kruskal 算法
    使用边集数组表示图，时间复杂度为
    边集数组结构为：[(weight, (begin, end))]
    weight: 权重
    begin: 起始顶点
    end: 结束顶点
    """
    g = graph
    n = g.nodenum
    # 定义一组数组，判断边与边是否形成环路: i位置对应的 reps[i]表示 路径从 i -> reps[i]
    reps = [i for i in range(n)]
    # 最小生成树
    mst = []

    # 图形的边集数组结构[(weight, (begin, end))]，按照权重weight 从小到大排序
    edges = g.edges
    edges.sort()

    for w, e in edges:
        begin, end = e
        ### resp[begin] == reps[end] 时，表示 形成环， 即 begin -> end -> reps[end] == reps[begin], begin -> reps[begin]
        if reps[begin] != reps[end]:
            mst.append((e, w))
            if len(mst) == n - 1:
                break

            # begin -> xxx = begin_end, end -> xxx = end_end
            begin_end, end_end = reps[begin], reps[end]
            for i in range(n):
                if reps[i] == end_end:
                    reps[i] = begin_end

    print '最小生成树：%s' %mst
    return mst

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
    # print '边集数组结构为：', g.edges

    MiniSpanTree_Kruskal(g)

