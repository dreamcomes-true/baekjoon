def solution(want, number, discount):
    
    cnt = 0
    n = sum(number)
    
    for i in range(len(discount)-n+1):
        
        temp_number = [0]*len(number)
        for j in range(i, i + n):
            if discount[j] in want:
                temp_number[want.index(discount[j])]+= 1
            else:
                break
        if temp_number == number :
            cnt +=1
            
    
    return cnt