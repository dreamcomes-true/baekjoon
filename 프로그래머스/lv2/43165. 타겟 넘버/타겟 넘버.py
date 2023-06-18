
def solution(numbers, target):
    
    parent_nodes = [0]
    
    for num in numbers : # 1
        temp = []
        for parent in parent_nodes :    # [4, -4]
            temp.append(parent + num)   # temp =  [4+1, 4-1, -4+1]
            temp.append(parent - num)   # temp = [4+1, 4-1, -4+1, -4-1]
        parent_nodes = temp
    
    cnt = 0
    for parent in parent_nodes :
        if parent == target :
            cnt +=1
    return cnt
