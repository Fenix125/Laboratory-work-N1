class PrimAlgo:
    def __init__(self, graph):
        self.edges = list(graph.edges(data=True))
    def prim(self, graph, start=0):
        visited_nodes = set()
        visited_nodes.add(start)
        res = []
        while len(visited_nodes) < len(graph.nodes):
                possible_edges = []
                for edge in self.edges:
                    if (edge[0] in visited_nodes and edge[1] not in visited_nodes) or\
                        (edge[0] not in visited_nodes and edge[1] in visited_nodes):
                        possible_edges.append(edge)
                possible_edges = sorted(possible_edges, key = lambda x: x[2]['weight'])
                res.append(possible_edges[0])
                visited_nodes.add(possible_edges[0][0])
                visited_nodes.add(possible_edges[0][1])
        return res
a = PrimAlgo(G)

a.prim(G)
b = [i[:2] for i in a.prim(G)]
