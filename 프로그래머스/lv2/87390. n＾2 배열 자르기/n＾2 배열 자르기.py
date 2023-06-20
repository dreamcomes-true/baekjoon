def making_group(i, n):
    nums = [i]*i
    for k in range(i+1, n+1):
        nums.append(k)
    return nums

def solution(n, left, right):
    
    # [1,2,3, 2,2,3, 3,3,3,] -> 0 1 2 / 3 4 5 / 
    # [1,2,3,4,5, 2,2,3,4,5, 3,3,3,4,5, 4,4,4,4,5, 5,5,5,5,5] -> 01234 / 56789
    
    #left 인덱스의 수 = left//n번째 그룹의 left%n 번째 수 -> 0번째 그룹의 2번째 수 
    #right 인덱스 수 = right//n번째 그룹의 right%n번째 수 -> 1번째 그룹의 2번째 수
    
    left_group, left_order = left//n, left%n
    right_group, right_order = right//n, right%n
    
    #0번째 그룹 1번째 수 ~ 1번째 그룹 2번째 수
    #[1,2,3],[2,2,3],[3,3,3]
    # (left_group+1)
    
    answer_list = []
    group_n = right_group - left_group
    for i in range(left_group, right_group+1):
        answer_list += making_group(i+1, n)
    answer_list = answer_list[left_order : group_n*n+right_order+1]
    
    
    return answer_list

'''
1 2 3 4 5 -> 1부터 i 까지
2 2 3 4 5 -> 2 2개 ~ i까지
3 3 3 4 5 -> 3 3개 ~ i까지
4 4 4 4 5 -> 4 4개 ~ i까지
5 5 5 5 5 -> 5 5개 ~ i까지
'''