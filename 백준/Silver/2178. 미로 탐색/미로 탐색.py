from collections import deque
n, m = list(map(int, input().split()))
miro = [list(map(int, list(input().strip()))) for _ in range(n)]
queue = deque([])
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        if x == n-1 and y == m-1 :
            break

        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1 :

                if miro[nx][ny] == 1 :
                    miro[nx][ny] = miro[x][y] + 1
                    queue.append((nx, ny))

bfs(0, 0)
print(miro[n-1][m-1])