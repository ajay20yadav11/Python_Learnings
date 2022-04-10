from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEgde(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance 

def dijkstar(graph, initial):
    visited = {initial: 0}       #set the starting point to zero and others to infinity

    path = defaultdict(list)    #to store unordered data like map format or graphs
    nodes = set(graph.nodes)    #to set values such as not repeating hence used set

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

        return visited, path


customdict = Graph()
customdict.addNode('a')
customdict.addNode('b')
customdict.addNode('c')
customdict.addNode('d')
customdict.addNode('e')
customdict.addEgde('a', 'b', 2)
customdict.addEgde('a', 'c', 3)
print(customdict.nodes)
print(customdict.edges)
print(customdict.distances)
print(dijkstar(customdict, 'a'))
