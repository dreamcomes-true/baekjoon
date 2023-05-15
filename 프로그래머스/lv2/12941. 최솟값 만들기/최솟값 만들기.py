def solution(A,B):
    A.sort()
    B.sort(reverse= True)
    num = 0
    for i in range(len(A)):
        num += A[i]*B[i]
    return num