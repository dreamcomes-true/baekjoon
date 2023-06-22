n = int(input())

game = []
for i in range(n) :
    game.append(list(map(int, input().split())))

# game = [[1, 1, 10], [1, 5, 1], [2, 2, -1]]

temp = [False] * n
visited = []
for i in range(n) :
    visited.append(temp[:])

# visited = [[False, False, False],[False, False, False],[False, False, False]]
is_win = False

def dfs(x, y) :
    global is_win 
    visited[x][y] = True
    jump = game[x][y] 
    if jump == -1 :
        is_win = True
        return
    if y+jump < n and visited[x][y+jump] == False :
        dfs(x, y+jump)
    if x+jump < n and visited[x+jump][y] == False :
        dfs(x+jump, y)
    return

answer = dfs(0,0)

if is_win == True :
    print("HaruHaru")
else:
    print("Hing")