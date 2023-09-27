t = int(input())
cases = []

for _ in range(t) :
    k = int(input())
    n = int(input())
    cases.append((k, n))

answer = []

for case in cases :
    # k층 n호에 몇명이 사는가
    k, n = case
    floor = [[i for i in range(1, n+1)]] # 0층의 1 - i호
    for i in range(1, k+1) : # k층에 대해서
        temp = []
        for j in range(1, n+1) : # 1부터 n호까지
            temp.append(sum(floor[i-1][:j]))
        floor.append(temp)
    answer.append(floor[-1][-1])

for i in answer :
    print(i)