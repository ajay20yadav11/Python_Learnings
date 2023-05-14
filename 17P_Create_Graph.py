class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addNode(self, vertex, edge):
        self.gdict[vertex].append(edge)


animated_dict = {"a": ["b", "c", "d"], "b": ["a", "e", "r"], "c": ["d", "e", "q", "a"]}


to_create_graph = Graph(animated_dict)
to_create_graph.addNode("b", "w")


print(to_create_graph.gdict)
