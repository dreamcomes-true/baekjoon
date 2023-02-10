def solution(A, B):
    A.sort()
    B.sort()
    cnt = 0
    starting_idx = 0
    for i in A:
        for j in range(starting_idx, len(B)):
            if i < B[j]:
                starting_idx = j+1
                cnt += 1
                break
            else:
                starting_idx = j+1
    return cnt
'''
A = 1, 4, 6, 8
B = 1, 3, 5, 9
'''