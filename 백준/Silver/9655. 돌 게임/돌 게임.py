
n = int(input())

sk_records = [0, 1, 0]
game_records = [False, True, False, True]

if n <= 3 :
    if game_records[n] :
        print('SK')
    else :
        print('CY')
else :
    for i in range(4, n+1) :
        take_one_lefts = i - 1
        take_three_lefts = i - 3
        if game_records[take_one_lefts] == True and game_records[take_three_lefts] == True :
            game_records.append(False)
        elif game_records[take_one_lefts] == False and game_records[take_three_lefts] == False :
            game_records.append(True)
        else :
            game_records.append(True)
    if game_records[-1] :
        print('SK')
    else :
        print('CY')



'''

돌이 1개일 때
game(1, 상근) - 상근이 우승
game(1, 창영) - 창영이 우승

돌이 2개일 때
game(2, 상근) - 창영이 우승
game(2, 창영) - 상근이 우승
상근이 1개 -> 창영이 1개

돌이 3개일 때
game(3, 상근) - 상근이 우승
game(3, 창영) - 창영이 우승
상근이 3개

돌이 4개일 때
game(4, 상근) - 창영 우승
game(4, 창영) - 상근 우승
1. 1개 가져갈 경우 - game(3, 창영) - 창영 우승 예상
2. 3개 가져갈 경우 - game(1, 창영) - 창영 우승 예상
즉, 어떻게 하든 창영 우승

돌이 5개 일때
game(5, 상근) - 상근 우승
game(5, 창영) - 창영 우승
1. 1개 가져갈 경우 - game(4, 창영) - 상근 우승
2. 3개 가져갈 경우 - game(2, 창영) - 상근 우승
'''