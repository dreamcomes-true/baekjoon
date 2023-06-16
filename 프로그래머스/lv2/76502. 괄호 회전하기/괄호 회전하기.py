def solution(s):
    strings = list(s)
    pair_dict = {"]" : "[", "}": "{", ")": "("}
    cnt = 0
    for n in range(len(s)) :
        is_correct = True
        stacks = []
        for i in strings : 
            if i in pair_dict.values() :
                stacks.append(i)
            else : 
                if stacks == [] or i not in pair_dict.keys() : 
                    is_correct = False
                    break    
                elif pair_dict[i] == stacks[-1] : 
                    stacks.pop(-1)
                else : 
                    is_correct = False
                    break        
        if stacks == [] and is_correct == True : 
            cnt += 1
        # 회전
        strings = strings[1:] + [strings[0]] 

    return cnt