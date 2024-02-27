import sys


class Edge:
    def __init__(self, start_node, end_node, weight):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight


class Graph:
    def __init__(self, n):
        self.num_nodes = n
        self.adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.graph_edges = []

    def size(self):
        return self.num_nodes

    def get_num_nodes(self):
        return self.num_nodes

    def get_adjacency_matrix(self):
        return self.adjacency_matrix

    def add_undirected_edge(self, from_node, to_node, val):
        self.adjacency_matrix[from_node][to_node] = val
        self.adjacency_matrix[to_node][from_node] = val
        self.graph_edges.append([from_node, to_node, val])

    def find(self, disjoint_set, node):
        if disjoint_set[node] == -1:
            return node
        return self.find(disjoint_set, disjoint_set[node])

    def join(self, disjoint_set, start_set, end_set):
        disjoint_set[start_set] = end_set

    @staticmethod
    def compare_edges(a, b):
        return a.weight < b.weight

    def kruskal(self):
        edges = []
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                if self.adjacency_matrix[i][j] > 0:
                    edges.append(Edge(i, j, self.adjacency_matrix[i][j]))

        edges.sort(key=lambda x: x.weight)

        mst = []
        disjoint_set = [-1] * self.num_nodes

        for edge in edges:
            start_set = self.find(disjoint_set, edge.start_node)
            end_set = self.find(disjoint_set, edge.end_node)

            if start_set != end_set:
                mst.append(edge)
                self.join(disjoint_set, start_set, end_set)

        min_cost = 0
        for edge in mst:
            min_cost += edge.weight
        return [[f"{i.start_node}-{i.end_node}" for i in mst], min_cost]

    def min_key(self, key, mst_set):
        min = sys.maxsize

        for v in range(self.num_nodes):
            if key[v] < min and mst_set[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def prim(self):
        key = [sys.maxsize] * self.num_nodes
        parent = [None] * self.num_nodes

        key[0] = 0
        mst_set = [False] * self.num_nodes

        parent[0] = -1

        for _ in range(self.num_nodes):
            u = self.min_key(key, mst_set)

            mst_set[u] = True

            for v in range(self.num_nodes):
                if (
                    self.adjacency_matrix[u][v] > 0
                    and mst_set[v] == False
                    and key[v] > self.adjacency_matrix[u][v]
                ):
                    key[v] = self.adjacency_matrix[u][v]
                    parent[v] = u

        min_cost = 0
        for i in range(1, self.num_nodes):
            min_cost += self.adjacency_matrix[i][parent[i]]
        return [[f"{parent[i]}-{i}" for i in range(1, self.num_nodes)], min_cost]
