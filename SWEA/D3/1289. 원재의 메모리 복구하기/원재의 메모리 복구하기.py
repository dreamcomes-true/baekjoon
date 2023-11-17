
def findLeastNumber(original) :
    # original = 0011
    # now = 0000
    now = '0'*len(original)
    cnt = 0
    for i in range(len(original)) :
        if original[i] != now[i] :
            cnt += 1
            now = now[:i] + original[i]*(len(original)-i)
    return cnt

testcaseNumber = int(input())
for i in range(testcaseNumber) :
    original = input()
    answer = findLeastNumber(original)
    print(f'#{i+1} {answer}')