#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
无向图的深度优先遍历算法DFS, 广度优先遍历算法BFS
"""
class Graph(object):
    """
        无向图：使用邻接矩阵创建图
        Python的图邻接矩阵法做为存储结构，0表示没有边，1表示有边，-1表示该节点为自己。
    """
    def __init__(self, maps = [], nodenum = 0, edgenum = 0):
        self.map = maps       #图的矩阵结构
        self.nodenum = len(maps)
        self.edgenum = edgenum
        #  self.nodenum = get_node_num()#节点数
        #  self.edgenum = get_edge_num()#边数

    def is_out_range(self, x):
        try :
            if x >= self.nodenum or x <= 0:
                raise IndexError
        except IndexError:
            print u'节点下标出界'

    def get_node_num(self):
        self.nodenum = len(self.map)
        return self.nodenum

    def get_edge_num(self):
        self.get_node_num()
        self.edgenum = 0
        for i in range(self.nodenum):
            for j in range(self.nodenum):
                if self.map[i][j] is 1:
                    self.edgenum = self.edgenum + 1
        return self.edgenum

    def add_node(self):
        for i in range(self.nodenum):
            self.map[i].append(0)
        self.nodenum = self.nodenum + 1
        ls = [0] * (self.nodenum - 1)
        ### -1 表示该节点为自己
        ls.append(-1)
        self.map.append(ls)

    def delete_node(self, x):
        # 假删除，只是归零而已
        for i in range(self.nodenum):
            if self.map[i][x] is 1:
                self.map[i][x] = 0
                self.edgenum = self.edgenum - 1
            if self.map[x][i] is 1:
                self.map[x][i] = 0
                self.edgenum = self.edgenum - 1

    def add_edge(self, x, y):
        # 由于是无向图，矩阵对称
        if self.map[x][y] is 0:
            # self.map[x][y] = 1
            self.map[y][x] = self.map[x][y] = 1
            self.edgenum = self.edgenum + 1

    def remove_edge(self, x, y):
        if self.map[x][y] is 1:
            self.map[x][y] = 0
            self.edgenum = self.edgenum - 1

    def depth_first_search(self):
        """
            递归实现 深度优先遍历
        """
        def dfs(self, i):
            order.append(i)
            visited[i] = 1
            for j in range(self.nodenum):
                if self.map[i][j] == 1 and visited[j] == 0:
                    dfs(self, j)

        order = []
        visited = [0] * self.nodenum
        for i in range(self.nodenum):
            if visited[i] == 0:
                dfs(self, i)
        print order
        return order

    def breadth_first_search(self):
        """
            队列实现 广度优先遍历
        """
        order = []
        queue = []
        visited = [0] * self.nodenum
        for i in range(self.nodenum):
            if visited[i] == 0:
                visited[i] = 1
                # 将节点加入 遍历表
                queue.append(i)
                order.append(i)
                while len(queue) != 0:
                    j = queue.pop(0)
                    for k in range(self.nodenum):
                        # 判断其他顶点与当前顶点存在边，且未访问过
                        if self.map[j][k] == 1 and visited[k] == 0:
                            visited[k] = 1
                            order.append(k)
                            queue.append(k)
        print order
        return order

if __name__ == '__main__':
    # 邻接矩阵实现图结构
    # maps = [[-1, 1, 0, 0],
    #         [0, -1, 0, 0],
    #         [0, 0, -1, 1],
    #         [1, 0, 0, -1]]
    # g = Graph(maps)
    g = Graph()
    # 生成4个顶点的图
    for i in range(5):
        g.add_node()

    print '初始化创建图形结构: ', g.map
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    # 添加第6个点
    g.add_node()
    g.add_edge(1, 4)
    print '添加边，顶点后的图形结构: ', g.map

    print '-'*20 + "深度优先遍历DFS" + '-'*20
    g.depth_first_search()

    print '-'*20 + "广度优先遍历DFS" + '-'*20
    g.breadth_first_search()
