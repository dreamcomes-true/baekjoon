from sys import stdin

n, k = map(int, stdin.readline().split())
lans = [int(stdin.readline().strip()) for _ in range(n)]
max_len = sum(lans) // k
min_len = 1
answer = 0

def check_ok(mid) :
    total = 0
    for lan in lans :
        total += (lan // mid)
    return total

# 이분 탐색
while True :

    mid = (max_len + min_len) // 2
    if mid == min_len :
        if check_ok(max_len) >= k :
            answer = max_len
        else :
            answer = min_len
        break

    total = check_ok(mid)

    if total >= k :
        min_len = mid
    else :
        max_len = mid - 1

print(answer)