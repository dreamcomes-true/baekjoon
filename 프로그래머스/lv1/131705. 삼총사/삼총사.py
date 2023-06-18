from itertools import combinations

def solution(number):
    cnt = 0
    three_nums = list(combinations(number, 3))
    for i in three_nums:
        if sum(i) == 0: 
            cnt += 1
    return cnt