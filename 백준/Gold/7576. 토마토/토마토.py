from collections import deque
from sys import stdin

m, n = map(int, stdin.readline().split())
tomato = []
done = []
for i in range(n) :
    temp = list(map(int, stdin.readline().split()))
    tomato.append(temp)
    for j in range(m) :
        if temp[j] == 1 :
            done.append((i, j))

queue = deque(done)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs() :

    while queue :
        node_x, node_y = queue.popleft()
        for i in range(4) :
            nx, ny = node_x + dx[i], node_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if tomato[nx][ny] == 0 :
                    tomato[nx][ny] = tomato[node_x][node_y] + 1
                    queue.append((nx, ny))

days = []
bfs()
max_day = 0
for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 0 :
            print(-1)
            exit()
        max_day = max(max_day, tomato[i][j])
print(max_day-1)