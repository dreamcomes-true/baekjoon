n, k = map(int, input().split())

answer = 1
for i in range(n-k+1, n+1) :
    answer *= i
divisor = 1
for i in range(1, k+1) :
    divisor *= i

if k == 0 :
    print(1)
else :
    print(answer//divisor)