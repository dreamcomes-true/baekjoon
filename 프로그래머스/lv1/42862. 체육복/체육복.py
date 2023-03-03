def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    # 여벌이 있는 학생이 도난당한 경우 제외
    new_reserve = list(set(reserve) - set(lost))
    new_lost = list(set(lost) - set(reserve))
    
    for i in new_reserve:
        if i-1 in new_lost : 
            new_lost.remove(i-1)
            
        elif i+1 in new_lost :
            new_lost.remove(i+1)
    
    return n - len(new_lost)
    