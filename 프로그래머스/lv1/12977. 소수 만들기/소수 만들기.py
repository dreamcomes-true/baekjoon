import itertools
import math
def solution(nums):
    cnt = 0
    for i in itertools.combinations(nums, 3):
        is_prime = True
        sums = sum(i)
        for j in range(2, int(math.sqrt(sums))+1):
            if sums % j == 0:
                is_prime = False
                break
        if is_prime == True:
            cnt += 1
    return cnt
                

'''
1, 2, 3, 4 => 4c3 가지 = 4
=> 1, 2, 3 / 1, 2, 4 / 1, 3, 4 / 2, 3, 4

1, 2, 7, 6, 5 => 5c3 = 5*4*3/3*2*1 = 10가지
1, 2, 7
1, 2, 6
1, 2, 5
1, 
'''