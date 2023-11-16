def calculateProfit(n, farms) :
    start = n//2
    end = n//2
    total = 0
    for floor in range(0, n//2) :
        total += sum(farms[floor][start:end+1])
        total += sum(farms[n-floor-1][start:end+1])
        start -= 1 
        end += 1 
    total += sum(farms[n//2])

    return total



testcaseNumber = int(input())

for i in range(testcaseNumber) :
    n = int(input())
    farms = []
    for j in range(n) :
        farms.append(list(map(int, list(input()))))
    answer = calculateProfit(n, farms)
    print(f'#{i+1} {answer}')