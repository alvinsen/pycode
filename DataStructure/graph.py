#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
python 数据结构之 图的表示方法
"""
class Graph_Matrix(object):
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
        def bfs(self, i, queue):
            queue.append(i)
            order.append(i)
            visited[i] = 1
            if len(queue) != 0:
                j = queue.pop(0)
                for k in range(self.nodenum):
                    if self.map[j][k] == 1 and visited[k] == 0:
                        bfs(self, k, queue)

        order = []
        queue = []
        visited = [0] * self.nodenum
        for i in range(self.nodenum):
            if visited[i] == 0:
                bfs(self, i, queue)

        print order
        return order


class Graph_Dict(object):
    """
        无向图：使用字典表示图
        比如有这么一张图：
            A -> B
            A -> C
            B -> C
            B -> D
            C -> D
            D -> C
            E -> F
            F -> C
        可以用字典和列表来构建
        graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    """
    def __init__(self, *args, **kwargs):
        self.node_neighbors = {}

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if not node in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self, edge):
        u, v = edge
        if(v not in self.node_neighbors[u]) and ( u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if u != v:
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.node_neighbors.has_key(start):
            return None
        for node in self.node_neighbors[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath: 
                    return newpath
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not self.node_neighbors.has_key(start):
            return []
        paths = []
        for node in self.node_neighbors[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.node_neighbors.has_key(start):
            return None
        shortest = None
        for node in self.node_neighbors[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


    def depth_first_search(self, root=None):
        order = []
        visited = {}
        def dfs(node):
            visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if n not in visited:
                    dfs(n)
        if root:
            dfs(root)

        for node in self.nodes():
            if node not in visited:
                dfs(node)

        print order
        return order

    def breadth_first_search(self,root=None):
        queue = []
        order = []
        visited = {}
        def bfs():
            while len(queue)> 0:
                node  = queue.pop(0)
                visited[node] = True
                for n in self.node_neighbors[node]:
                    if n not in visited and n not in queue:
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.nodes():
            if node not in visited:
                queue.append(node)
                order.append(node)
                bfs()
        print order

        return order

if __name__ == '__main__':
    ### 邻接矩阵表示图
    g = Graph_Matrix()
    # 生成4个顶点的图
    for i in range(8):
        g.add_node()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 7)
    g.add_edge(4, 7)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(5, 6)
    print '图形结构: ', g.map

    print '-'*20 + "深度优先遍历DFS" + '-'*20
    g.depth_first_search()

    print '-'*20 + "广度优先遍历DFS" + '-'*20
    g.breadth_first_search()

    print '+' * 100

    ### 图的深度广度优先遍历
    g = Graph_Dict()
    g.add_nodes([i+1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((5, 6))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    print 'nodes: ', g.nodes()
    #### 查找路径
    print 'find_path: ', g.find_path(1, 7)
    print 'find_all_paths: ', g.find_all_paths(1, 7)
    print 'find_shortest_path: ', g.find_shortest_path(1, 7)

    print '-'*20 + "深度优先遍历DFS" + '-'*20
    g.depth_first_search()

    print '-'*20 + "广度优先遍历DFS" + '-'*20
    g.breadth_first_search()

