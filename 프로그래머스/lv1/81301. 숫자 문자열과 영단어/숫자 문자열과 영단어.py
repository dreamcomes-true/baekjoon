def solution(s):
    answer = ""
    numstring = ""
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in s :
        if i not in ['0','1','2','3','4','5','6','7','8','9']:
            numstring += i
            if numstring in numbers :
                answer += str(numbers.index(numstring))
                numstring = ""
        else :
            if numstring != "" : 
                answer += str(numbers.index(numstring))
                answer += i
                numstring = ""
            else :
                answer += i
                
            
    return int(answer)