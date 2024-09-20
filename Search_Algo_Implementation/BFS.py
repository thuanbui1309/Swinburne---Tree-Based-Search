from collections import OrderedDict, deque

graph = {
    0 : [1, 2],
    1 : [0, 3],
    2 : [0, 3],
    3 : [0, 1, 2, 3, 4],
    4 : [3]
}

class BFS:
    def __init__(self, graph):
        self.visited = OrderedDict()
        self.graph = graph

    def search(self, vertex):
        vertexs = deque([vertex])

        while len(vertexs) > 0:
            v = vertexs.popleft()

            if v not in self.visited:
                self.visited[v] = True

                for neighbor in self.graph[v]:
                    if (neighbor not in self.visited):
                        vertexs.append(neighbor)

    def showPath(self, vertex):
        self.search(vertex)

        for key, value in self.visited.items():
            print(key, end=" ")
        print()

        self.visited = OrderedDict()

# bFS = BFS(graph)

# while True:
#     vertex = int(input("Enter: "))
#     bFS.showPath(vertex)