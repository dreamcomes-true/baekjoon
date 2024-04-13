from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(n)]



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs() :
    global answer

    queue = deque([])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                queue.append((i, j))

    tmp_map = [row[:] for row in maps]

    while queue :

        x, y = queue.popleft()

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1 :
                if tmp_map[nx][ny] == 0:
                    tmp_map[nx][ny] = 2
                    queue.append((nx, ny))

    safe_cnt = 0
    for i in range(n) :
        safe_cnt+=tmp_map[i].count(0)

    answer = max(safe_cnt, answer)

answer = 0
# 모든 벽의 조합 구하기
def make_wall(nums) :
    if nums == 3 :
        bfs()
        return

    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == 0 :
                maps[i][j] = 1 # 벽을 세운다
                make_wall(nums+1)
                maps[i][j] = 0 # 원상복귀


make_wall(0)
print(answer)