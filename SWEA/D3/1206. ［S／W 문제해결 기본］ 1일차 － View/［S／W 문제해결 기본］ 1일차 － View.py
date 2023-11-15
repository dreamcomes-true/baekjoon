def findGoodViewNumber(aparts) :
    goodView = 0
    for i in range(len(aparts)) :
        if aparts[i] != 0 :
            total_floor = aparts[i]
            for floor in range(1, total_floor + 1) :
                # 1층
                if aparts[i-2] < floor and aparts[i-1] < floor and aparts[i+1] < floor and aparts[i+2] < floor :
                    goodView += 1
    return goodView

for i in range(10) :
    n = int(input())
    aparts = list(map(int, input().split()))
    answer = findGoodViewNumber(aparts)
    print(f'#{i+1} {answer}')

