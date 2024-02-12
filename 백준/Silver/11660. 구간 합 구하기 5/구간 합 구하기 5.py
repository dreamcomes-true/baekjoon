import sys
input = sys.stdin.readline

# 실제 num list 입력 받기
n, m = map(int, input().split())
num_list = []
for i in range(n) :
    num_list.append(list(map(int, input().split())))

# 누적합 list 만들기 - O(N^2)
sum_list = []
first_sum = []
total = 0
for num in num_list[0] :
    total += num
    first_sum.append(total)
sum_list.append(first_sum)

for x in range(1, n) :
    temp = []
    for y in range(n) :
        if y == 0 :
            temp.append(sum_list[x-1][y] + num_list[x][y])
        else :
            temp.append(temp[-1] + sum_list[x-1][y] - sum_list[x-1][y-1] + num_list[x][y])
    sum_list.append(temp)

# M 개에 대한 누적합 구하기 - O(M)

for i in range(m) :
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1 :
        print(sum_list[x2-1][y2-1])
    elif x1 == 1 :
        print(sum_list[x2-1][y2-1] - sum_list[x2-1][y1-2])
    elif y1 == 1 :
        print(sum_list[x2-1][y2-1] - sum_list[x1-2][y2-1])
    else :
        print(sum_list[x2-1][y2-1] - sum_list[x2-1][y1-2] - sum_list[x1-2][y2-1] + sum_list[x1-2][y1-2])