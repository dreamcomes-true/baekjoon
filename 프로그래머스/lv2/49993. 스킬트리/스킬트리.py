import copy

def solution(skill, skill_trees):
    skill = list(skill)
    cnt = 0
    for case in skill_trees: #'bda'
        skill2 = copy.deepcopy(skill)
        is_ok = True
        for i in case: #'b'
            if i in skill2 :
                if i != skill2.pop(0):
                    is_ok = False
                    break
        if is_ok == True:
            cnt += 1
        
    return cnt
                
            
    
    
    '''
    skill = list(skill) # c, b, d
    cnt = 0
    for case in skill_trees:
        starting_index = 0
        is_ok = True
        for i in range(len(case)) :
            if case[i] in skill : 
                stack = [case[i]] # ['b']
                starting_index = i+1 # 1
                break

        if skill.index(stack[0]) != 0 :
            print(case, skill.index(stack[0]))
            is_ok = False
        else:
            for i in range(starting_index, len(case)): # 'bacde'
                if case[i] not in skill:
                    continue
                if skill.index(case[i]) > skill.index(stack[-1]) :
                    stack.append(case[i]) 
                else :
                    is_ok = False
                    break
                
        if is_ok == True:
            cnt += 1
            
    return cnt
    '''
