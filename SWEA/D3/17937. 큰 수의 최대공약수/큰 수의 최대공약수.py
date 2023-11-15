testcaseNumber = int(input())

for i in range(testcaseNumber) :
    a, b = map(int, input().split()) # a, b 는 상당히 큰 범위.
    if a == b :
        answer = a
    else :
        answer = 1
    print(f'#{i+1} {answer}')