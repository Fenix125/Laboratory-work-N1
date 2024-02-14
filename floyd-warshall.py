class floyd_warshall:
    def __init__(self, graph):
        self.graph = graph
        self.matrix = self.graph_to_matr()
    def graph_to_matr(self):
        edges = list(self.graph.edges(data = True))
        n = len(self.graph.nodes())
        matrix = [[float('inf') for i in range(n)] for j in range(n)]
        for edge in edges:
            matrix[edge[0]][edge[1]] = edge[2]['weight']
        for i in range(n):
            matrix[i][i] = 0
        return matrix
    def floyd_warshall(self):
        length = len(self.matrix)
        res = self.matrix.copy()
        for k in range(length):
            for i in range(length):
                for j in range(length):
                    res[i][j] = min(res[i][j], res[i][k] + res[k][j])
        dict_res = {}
        for row_i, row in enumerate(res):
            dict_res[row_i] = {el_i:el for el_i, el in enumerate(row)}


        return dict_res
a = floyd_warshall(G)
print(a.floyd_warshall())
