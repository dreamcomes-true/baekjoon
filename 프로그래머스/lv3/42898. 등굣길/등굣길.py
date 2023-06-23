def solution(m, n, puddles):
    
    roads = [[0]*m for i in range(n)]
    for puddle in puddles :
        x, y = puddle
        roads[y-1][x-1] = -1
    
    roads[0][0] = 1
            
    for i in range(len(roads)):
        for j in range(len(roads[0])):
            if roads[i][j] == -1 :
                pass
            else :
                if i == 0 or roads[i-1][j] == -1 :
                    up = 0
                else :
                    up = roads[i-1][j]
                if j == 0 or roads[i][j-1] == -1 :
                    left = 0
                else :
                    left = roads[i][j-1]
                roads[i][j] += (up + left)
             
    return roads[n-1][m-1] % 1000000007