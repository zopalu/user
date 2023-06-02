import sys

def prim_mst(graph):
    n = len(graph)
    mst = [False] * n
    key = [sys.maxsize] * n
    parent = [None] * n

    key[0] = 0  # Start with the first vertex

    for _ in range(n):
        u = min_key_vertex(key, mst)
        mst[u] = True

        for v in range(n):
            if graph[u][v] > 0 and not mst[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent #parent the parent array is returned, which represents the MST.

def min_key_vertex(key, mst):
    min_value = sys.maxsize
    min_index = -1

    for v in range(len(key)):
        if not mst[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v

    return min_index

# Example usage:
graph = [
    [0,5,9,7,0,0,4],
    [5,0,10,0,8,21,0],
    [9,10,0,20,25,0,0],
    [7,0,20,0,11,0,6],
    [0,8,25,11,0,30,0],
    [0,21,0,0,30,0,0],
    [4,0,0,6,0,0,0]
]
mst = prim_mst(graph)
print("Edge   Weight")
for i in range(1, len(graph)):
    print(mst[i], "-", i, "   ", graph[i][mst[i]])
