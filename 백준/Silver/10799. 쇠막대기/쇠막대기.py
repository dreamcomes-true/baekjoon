from sys import stdin

parenthesis = stdin.readline()
opening, closing = '(', ')'
bar = 0
pieces = 0
for idx, value in enumerate(parenthesis) :
    if value == opening :
        bar += 1
        pieces += 1
    if value == closing and parenthesis[idx-1] == opening : # 레이저인 경우
        bar -= 1
        pieces -= 1
        pieces += bar
    if value == closing and parenthesis[idx-1] == closing :
        bar -= 1

print(pieces)