n, k = map(int, input().split())


dynamic_programming = [[0 for i in range(n)] for i in range(k)]

for i in range(n) :
    dynamic_programming[0][i] = 1
for i in range(k) :
    dynamic_programming[i][0] = i+1

for i in range(1, k) :
    for j in range(1, n) :
        dynamic_programming[i][j] = dynamic_programming[i][j-1] + dynamic_programming[i-1][j]

print(dynamic_programming[k-1][n-1] % 1000000000)