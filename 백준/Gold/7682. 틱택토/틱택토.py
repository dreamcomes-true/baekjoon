
def find_winner(tictacto) :
    winner = []
    if tictacto[0] == tictacto[4] == tictacto[8] == 'X' :
        winner.append('X')
    elif tictacto[2] == tictacto[4] == tictacto[6] == 'X' :
        winner.append('X')
    elif tictacto[0] == tictacto[1] == tictacto[2] == 'X' :
        winner.append('X')
    elif tictacto[3] == tictacto[4] == tictacto[5] == 'X' :
        winner.append('X')
    elif tictacto[6] == tictacto[7] == tictacto[8] == 'X' :
        winner.append('X')
    elif tictacto[0] == tictacto[3] == tictacto[6] == 'X' :
        winner.append('X')
    elif tictacto[1] == tictacto[4] == tictacto[7] == 'X' :
        winner.append('X')
    elif tictacto[2] == tictacto[5] == tictacto[8] == 'X' :
        winner.append('X')

    if tictacto[0] == tictacto[4] == tictacto[8] == 'O' :
        winner.append('O')
    elif tictacto[2] == tictacto[4] == tictacto[6] == 'O' :
        winner.append('O')
    elif tictacto[0] == tictacto[1] == tictacto[2] == 'O' :
        winner.append('O')
    elif tictacto[3] == tictacto[4] == tictacto[5] == 'O' :
        winner.append('O')
    elif tictacto[6] == tictacto[7] == tictacto[8] == 'O' :
        winner.append('O')
    elif tictacto[0] == tictacto[3] == tictacto[6] == 'O' :
        winner.append('O')
    elif tictacto[1] == tictacto[4] == tictacto[7] == 'O' :
        winner.append('O')
    elif tictacto[2] == tictacto[5] == tictacto[8] == 'O' :
        winner.append('O')

    if len(winner) > 1 :
        return (False, 2)
    elif len(winner) == 1 :
        return (True, winner[0])
    else :
        return (False, 0)

while True :
    tictacto = input()
    if tictacto == 'end' :
        break

    x = tictacto.count('X')
    o = tictacto.count('O')
    blank = tictacto.count('.')

    answer = find_winner(tictacto)
    if x == o+1 and answer == (True, 'X') :
        print('valid')
        continue
    elif x == o and answer == (True, 'O') :
        print('valid')
        continue
    elif (x == o+1 or x == o) and answer == (False, 0) and blank == 0 :
        print('valid')
        continue

    print('invalid')