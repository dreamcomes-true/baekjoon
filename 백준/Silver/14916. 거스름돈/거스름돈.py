cash = int(input())
money = [0, -1, 1, -1, 2, 1]

for i in range(6, cash+1) :
    five_left = i - 5
    two_left = i - 2
    if money[five_left] != -1 :
        money.append(1+money[five_left])
    elif money[two_left] != -1 :
        money.append(1+money[two_left])
    else :
        money.append(-1)

print(money[cash])

'''
동전의 개수가 최소가 되도록 거슬러 준다

money(1) : -1 (불가)
money(2) : 1개
money(3) : -1 (불가)
money(4) : 2개
money(5) : 1개
money(6) : 3개
5원 -> 남은돈 money(1) = 불가능
2원 -> 남은돈 money(4) = 1 + 2 = 3
money(7) : 2개
5원 -> 남은돈 money(2) = 1 + 1 = 2개
money(8) : 4개
5원 -> money(3) = 불가능
2원 -> money(6) = 1 + 3 = 4개
'''
