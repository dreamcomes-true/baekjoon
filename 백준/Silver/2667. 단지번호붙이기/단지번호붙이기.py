num = int(input())

houses = []
for i in range(num) :
    houses.append(list(map(int, list(input()))))

visited = [[False]*num for i in range(num)]

# DFS
def dfs(x, y) :
    visited[x][y] = True
    up, left, right, down = 0, 0, 0, 0
    if x >= 1 and houses[x-1][y] == 1 and visited[x-1][y] == False :
        up = dfs(x-1, y)
    if y >= 1 and houses[x][y-1] == 1 and visited[x][y-1] == False :
        left = dfs(x, y-1)
    if y < num -1 and houses[x][y+1] == 1 and visited[x][y+1] == False :
        right = dfs(x, y+1)
    if x < num - 1 and houses[x+1][y] == 1 and visited[x+1][y] == False :
        down = dfs(x+1, y)
    return up + left + right + down + 1

count_list = []
for y in range(num) :
    for x in range(num) :
        if houses[x][y] == 1 and visited[x][y] == False :
            count = dfs(x, y)
            count_list.append(count)

count_list.sort()
print(len(count_list))
for i in count_list:
    print(i)
