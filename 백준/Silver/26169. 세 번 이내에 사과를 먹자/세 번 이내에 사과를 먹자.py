game = []
for i in range(5): 
    game.append(list(map(int, input().split())))

x, y = map(int, input().split())
# [[0,0,1,0,0],[0,0,-1,0,0],[0,0,1,0,0],[1,1,-1,1,0],[0,0,0,-1,0]]

cnt = 0
move = -1
cantgo = []
is_win = False

def dfs(x, y) :
    global cnt, move, is_win

    # 이동횟수 추가
    move += 1

    # 지나온 길 리스트에 추가
    cantgo.append((x,y))
    
    # 사과일 경우 사과 먹기
    if game[x][y] == 1 :
        cnt += 1
    
    # 사과 2개 이상인 경우 리턴
    if cnt >= 2 :
        is_win = True
        return

    # 이동횟수 3회 이하 제한
    if move == 3 :
        cantgo.remove((x,y))
        move -= 1
        if game[x][y] == 1:
            cnt -= 1
        return
    
    if x+1 < 5 and game[x+1][y] != -1 and (x+1,y) not in cantgo:
        dfs(x+1, y)
        if is_win == True:
            return
    if x-1 >= 0 and game[x-1][y] != -1 and (x-1,y) not in cantgo:
        dfs(x-1, y)
        if is_win == True:
            return
    if y+1 < 5 and game[x][y+1] != -1 and (x,y+1) not in cantgo:
        dfs(x, y+1)
        if is_win == True:
            return
    if y-1 >= 0 and game[x][y-1] != -1 and (x,y-1) not in cantgo:
        dfs(x, y-1)
        if is_win == True:
            return
    cantgo.remove((x, y))
    move -= 1
    if game[x][y] == 1:
            cnt -= 1
    return


dfs(x, y)

if is_win == True:
    print(1)
else:
    print(0)