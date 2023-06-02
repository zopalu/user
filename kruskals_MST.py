class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y) #to avoid looop

        return result

# Example usage:
g = Graph(7)
g.add_edge(0, 1, 28)
g.add_edge(0, 5, 10)
g.add_edge(1, 2, 16)
g.add_edge(1, 6, 14)
g.add_edge(2, 3, 12)
g.add_edge(3, 6, 18)
g.add_edge(3, 4, 22)
g.add_edge(4, 5, 25)
g.add_edge(4, 6, 24)

mst = g.kruskal_mst()
print("Edge   Weight")
for u, v, weight in mst:
    print(u, "-", v, "   ", weight)
