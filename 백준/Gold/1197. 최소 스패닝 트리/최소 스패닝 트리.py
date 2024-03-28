import heapq

def prim(edges, v, e) :

    visited = [False] * (v+1)
    ways = [(0, 1)]
    total_cost = 0
    cnt = 0

    while ways and cnt < v :

        cost, vertex = heapq.heappop(ways)
        if visited[vertex] == True:
            continue

        visited[vertex] = True
        total_cost += cost
        cnt += 1

        for cost, vertex in edges[vertex] :
            if visited[vertex] == False:
                heapq.heappush(ways, (cost, vertex))

    return total_cost

v, e = map(int, input().split()) # 정점 v, 간선 e
edges = [[] for _ in range(v+1)]

for _ in range(e) :
    a, b, cost = map(int, input().split())
    edges[a].append((cost, b))
    edges[b].append((cost, a))

print(prim(edges,v,e))