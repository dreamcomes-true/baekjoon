n, m = map(int, input().split())
floors = []
for i in range(n):
    floors.append(list(input()))


false_list = [False]*m
visited=[]
for i in range(n):
    visited.append(false_list[:])
cnt = 0

def dfs(x,y) :
    visited[x][y] = True
    if floors[x][y] == '|':
        if x < n-1 and floors[x+1][y] == '|' and visited[x+1][y] == False:
            dfs(x+1, y)
        else:
            return
    elif floors[x][y] == '-' :
        if y < m-1 and floors[x][y+1] == '-' and visited[x][y+1] == False:
            dfs(x, y+1)
        else:
            return

for i in range(n):
    for j in range(m):
        if visited[i][j] == False :
            dfs(i, j)
            cnt += 1
print(cnt)