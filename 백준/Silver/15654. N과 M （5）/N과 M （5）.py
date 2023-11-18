n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

answer = []

def backtracking() :

    if len(answer) == m :
        print(" ".join(map(str, answer)))
        return;

    for i in nums : 

        if i not in answer :
            answer.append(i)
            backtracking()
            answer.pop()
backtracking()