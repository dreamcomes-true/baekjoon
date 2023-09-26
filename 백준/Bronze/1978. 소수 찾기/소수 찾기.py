import math

n = int(input())

numbers = list(map(int, input().split()))
cnt = 0
for num in numbers :
    is_sosu = True
    if num == 1 :
        pass
    else :
        for i in range(2, int(math.sqrt(num))+1) : 
            if num % i == 0 :
                is_sosu = False
                break
        if is_sosu == True :
            cnt += 1

print(cnt)