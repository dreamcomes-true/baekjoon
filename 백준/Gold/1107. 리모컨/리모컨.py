n = int(input()) 
m = int(input())

if m == 0: 
    broken_nums = []
else:
    broken_nums = list(map(int, input().split()))

min_count = abs(n - 100) 

for num in range(1000000) :
    is_ok = True
    for i in str(num) :
        if int(i) in broken_nums :
            is_ok = False
            break
    if is_ok == True :
        if abs(n - num) + len(str(num)) < min_count :
            min_count = abs(n - num) + len(str(num))

print(min_count)