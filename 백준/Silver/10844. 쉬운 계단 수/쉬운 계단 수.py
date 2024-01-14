
n = int(input())
dynamic_programming = [[0] * 10 for i in range(n+1)]
for i in range(1, 10) :
    dynamic_programming[1][i] = 1

# dynamic_programming = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1], ..]

for i in range(2, n + 1) : # 계단 수가 i 일 때
    for last in range(0, 10) : # 끝자리가 0부터 9인 경우 각각 끝자리 j일때
        if last == 0 :
            dynamic_programming[i][last] = dynamic_programming[i-1][last+1]
        elif last == 9 :
            dynamic_programming[i][last] = dynamic_programming[i-1][last-1]
        else : # 끝자리 1 ~ 8 인 경우
            dynamic_programming[i][last] = dynamic_programming[i-1][last-1] + dynamic_programming[i-1][last+1]
print(sum(dynamic_programming[-1]) % 1000000000)
