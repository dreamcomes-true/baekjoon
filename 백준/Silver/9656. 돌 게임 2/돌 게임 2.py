
starter_win = [0, False, True, False]

n = int(input())

for i in range(4, n + 1) :
    take_one = i - 1
    take_three = i - 3
    if starter_win[take_one] and starter_win[take_three] :
        starter_win.append(False)
    else :
        starter_win.append(True)

if starter_win[n] :
    print('SK')
else:
    print('CY')