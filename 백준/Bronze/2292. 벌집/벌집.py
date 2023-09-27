
n = int(input())
cnt = 2
before = 1

if n == 1 :
    print(1)
else:
    while True :
        if n <= before + (cnt * 6 - 6) :
            break
        before = before + (cnt * 6 - 6)
        cnt += 1
    print(cnt)
