import copy

def solution(k, tangerine) :
    tangerine_dict = {}
    for i in tangerine :
        if i in tangerine_dict :
            tangerine_dict[i] += 1
        else :
            tangerine_dict[i] = 1
    tangerine_dict = dict(sorted(tangerine_dict.items(), key=lambda x:x[1]))
    
    remove_goal = len(tangerine) - k    # 제거 개수
    
    answer_dict = copy.deepcopy(tangerine_dict)
    
    for items in tangerine_dict.items() :
        if items[1] <= remove_goal : 
            remove_goal -= items[1]
            del answer_dict[items[0]]
        else :
            answer_dict[items[0]] -= remove_goal
            remove_goal = 0
        if remove_goal == 0 :
            break
            
    return len(answer_dict.keys())


