import sys

n, m, r = map(int, sys.stdin.readline().split())

network = [[i] for i in range(n)]
visited = [False]*n
result = [0]*n
for i in range(m) :
    x, y = map(int, sys.stdin.readline().split())
    network[x-1].append(y-1)
    network[y-1].append(x-1)

# network = [[0,3,2],[1,0,2,3],[2,1,3],[3,0,1,2],[4]]


queue = []

def bfs(v):
    cnt = 0
    visited[v] = True
    queue.append(v)
    while queue != [] :
        v = queue.pop(0)
        cnt += 1
        result[v] = cnt
        network[v].sort()
        for i in network[v] :
            if visited[i] == False:
                visited[i] = True
                queue.append(i)


bfs(r-1)

for i in result:
    print(i)