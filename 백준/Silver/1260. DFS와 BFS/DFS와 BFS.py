n, m, v = map(int, input().split())

adj_list = [[] for _ in range(n+1)]

for i in range(m) :
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, n+1) :
    adj_list[i].sort()


# DFS

visited = [False] * (n+1)

def dfs(v) :
    for i in adj_list[v] :
        if visited[i] == True : 
            pass
        else: 
            visited[i] = True
            print(i, end= ' ')
            dfs(i)

print(v, end= ' ')
visited[v] = True
dfs(v)

# BFS

print('')
visited = [False] * (n+1)
queue = []

def bfs(v) :
    visited[v] = True
    queue.append(v)

    while queue != [] :
        i = queue.pop(0)
        print(i, end = ' ')
        for j in adj_list[i]: 
            if visited[j] == False :
                visited[j] = True
                queue.append(j)

bfs(v)