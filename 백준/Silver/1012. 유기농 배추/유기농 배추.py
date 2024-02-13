
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(x, y) :
    visited[x][y] = True

    if y > 0 and farm[x][y-1] == 1 and visited[x][y-1] == False :
        dfs(x, y-1)
    if y < m-1 and farm[x][y+1] == 1 and visited[x][y+1] == False :
        dfs(x, y+1)
    if x > 0 and farm[x-1][y] == 1 and visited[x-1][y] == False :
        dfs(x-1, y)
    if x < n-1 and farm[x+1][y] == 1 and visited[x+1][y] == False :
        dfs(x+1, y)

    return

# test case 개수 입력
test_n = int(input())

# 배추밭 정보 입력 받고 farm 리스트 생성
for test in range(test_n) :

    m, n, k = map(int, input().split())
    farm = [[0]*m for i in range(n)]
    visited = [[False]*m for i in range(n)]
    for _ in range(k) :
        x, y = map(int, input().split())
        farm[y][x] = 1

    # DFS
    count = 0
    for i in range(n) :
        for j in range(m) :
            if farm[i][j] == 1 and visited[i][j] == False :
                count += 1
                dfs(i, j)

    print(count)