n, m = map(int, input().split())
numlist = []

def backtracking() :
    
    if len(numlist) == m:
        print(" ".join(map(str, numlist)))
    
    for i in range(1, n+1) : # 1부터 n까지의 수에 대해서
        if i not in numlist : # i가 numlist에 없을 때,
            if len(numlist) == 0 :
                numlist.append(i)
            elif numlist[-1] < i :
                numlist.append(i)   
            else :
                continue
            backtracking()
            numlist.pop()
        
backtracking()
