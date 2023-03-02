def solution(nums):
    n = len(nums)/2
    nums_set = list(set(nums)) # 중복 제거
    if len(nums_set) >= n : 
        return n
    elif len(nums_set) < n :
        return len(nums_set)
    
