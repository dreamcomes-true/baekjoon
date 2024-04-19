from sys import stdin
case = 1
while True :
    n = int(stdin.readline())
    if n == 0 :
        break
    tetris = [list(map(int, stdin.readline().split())) for _ in range(n)]
    max_value = sum(tetris[0][0:4])
    # 1. 1 X 4 유형
    for x in range(n) : # y가 0부터 n-1일 때

        for y in range(0, n-4) :
            sum_value = sum(tetris[x][y:y+4])
            if max_value < sum_value :
                max_value = sum_value
                
    # 2. 4 X 1 유형
    for y in range(n) :
        for x in range(0, n-4) :
            sum_value = sum([tetris[i][y] for i in range(x, x+4)])
            if max_value < sum_value :
                max_value = sum_value

    # 3. 2 X 3 유형
    for x in range(n-1) :
        for y in range(0, n-2) :
            # 1) 두번쨰 블록 가로
            sum_value = sum(tetris[x][y:y+2])
            sum_value += sum(tetris[x+1][y+1:y+3])
            if max_value < sum_value :
                max_value = sum_value

            # 2) 세번째 블록 가로
            sum_value = sum(tetris[x][y:y+3])
            sum_value += tetris[x+1][y+2]
            if max_value < sum_value :
                max_value = sum_value

            # 3) 네 번째 블록 가로
            sum_value -= tetris[x+1][y+2]
            sum_value += tetris[x+1][y+1]
            if max_value < sum_value :
                max_value = sum_value

            # 3) 세번째 블록 가로
            sum_value = sum(tetris[x+1][y:y+3])
            sum_value += tetris[x][y]
            if max_value < sum_value :
                max_value = sum_value

            # 4) 네번째 블록 가로
            sum_value -= tetris[x][y]
            sum_value += tetris[x][y+1]
            if max_value < sum_value :
                max_value = sum_value



    # 4. 3 X 2 유형
    for y in range(n-1) :
        for x in range(0, n-2) :

            # 1) 두번째 블록 세로
            sum_value = sum([tetris[i][y] for i in range(x+1, x+3)])
            sum_value += sum([tetris[i][y+1] for i in range(x, x+2)])
            if max_value < sum_value :
                max_value = sum_value

            # 2) 세번째 블록 세로
            sum_value = sum(tetris[i][y+1] for i in range(x, x+3))
            sum_value += tetris[x+2][y]
            if max_value < sum_value :
                max_value = sum_value

            # 3) 네번쨰 블록 세로
            sum_value -= tetris[x+2][y]
            sum_value += tetris[x+1][y]
            if max_value < sum_value :
                max_value = sum_value

            # 4) 세번째 블록
            sum_value = sum([tetris[i][y] for i in range(x, x+3)])
            sum_value += tetris[x][y+1]
            if max_value < sum_value :
                max_value = sum_value

            # 5) 네 번째 블록
            sum_value -= tetris[x][y+1]
            sum_value += tetris[x+1][y+1]
            if max_value < sum_value :
                max_value = sum_value

    # 5. 2 x 2 유형
    for x in range(n-1) :
        for y in range(n-1) :
            sum_value = sum(tetris[x][y:y+2])
            sum_value += sum(tetris[x+1][y:y+2])
            if max_value < sum_value :
                max_value = sum_value

    print(f'{case}. {max_value}')
    case += 1
