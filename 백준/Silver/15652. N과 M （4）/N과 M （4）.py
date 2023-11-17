n, m = map(int, input().split())

numlist = []

def backtracking() :
    if len(numlist) == m :
        print(" ".join(map(str, numlist)))
        return;

    for i in range(1, n+1) :    # 1부터 n까지의 숫자에 대해서
        if len(numlist) == 0:
            numlist.append(i)
        elif numlist[-1] <= i :
            numlist.append(i)
        else:
            continue
        backtracking()
        numlist.pop()

backtracking()
