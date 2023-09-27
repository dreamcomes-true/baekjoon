n, m = map(int, input().split()) 

board = []
for _ in range(n) :
    board.append(input())

total_cases = []
for i in range(n-7) :
    for j in range(m-7) :
        temp_board = [] 
        for row in range(i, i+8) :
            temp_board.append(board[row][j:j+8])
        total_cases.append(temp_board)


# 다시 칠해야 하는 정사각형 개수를 리턴하는 함수
def check_refill(board, start) :
    cnt = 0
    if start == 'W' :
        answer_board = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
        for i in range(8) :
            for j in range(8) :
                if board[i][j] != answer_board[i][j] :
                    cnt+= 1
    else :
        answer_board = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
        for i in range(8) :
            for j in range(8) :
                if board[i][j] != answer_board[i][j] :
                    cnt+= 1
    return cnt

answer_list = []


for case in total_cases :
    white_cnt = check_refill(case, 'W')
    black_cnt = check_refill(case, 'B')
    answer_list.append(min(white_cnt, black_cnt))

print(min(answer_list))
