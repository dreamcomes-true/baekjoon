from collections import deque

n = int(input())  
apple_n = int(input()) 
board =  [[0 for i in range(n)] for j in range(n)]

for i in range(apple_n) :
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

convert_n = int(input()) 
converts_arr = []
for i in range(convert_n) :
    time, convert = input().split()
    converts_arr.append((int(time), convert))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
curr_time, i = 0, 0
x, y = 0, 0
snake = deque()    
snake.append((x, y)) 

while True :
    curr_time += 1
    x, y = x + dx[direction], y + dy[direction] 

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if (x,y) in snake:
        break

    if board[x][y] == 1 :
        snake.append((x, y)) 
        board[x][y] = 0
    else :
        snake.append((x, y)) 
        snake.popleft()
    
    if curr_time == converts_arr[i][0] :
        if converts_arr[i][1] == 'L' :
            direction = (direction -1) % 4
        else :
            direction = (direction + 1) % 4

        if i < len(converts_arr) -1 :
            i += 1
print(curr_time)
