n = int(input())
m = int(input())
cnt = 0

network = [[i] for i in range(n)]
visited = [False]*n

def dfs(x) :
    visited[x] = True
    global cnt
    cnt += 1
    for i in network[x] : 
        if visited[i] == False:
            dfs(i)
    return

for i in range(m):
    x, y = map(int, input().split())
    network[x-1].append(y-1)
    network[y-1].append(x-1)

dfs(0)

print(cnt-1)