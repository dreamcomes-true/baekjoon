def solution(progresses, speeds):
    
    answer = {}
    
    for i in range(len(speeds)):
        work_days = (100-progresses[i]) // speeds[i] 
        if (100-progresses[i]) % speeds[i] != 0 :
            work_days += 1
        if answer == {} :
            answer[work_days] = 1
        elif work_days <= max(answer.keys()):
            answer[max(answer.keys())] += 1
        else :
            answer[work_days] = 1
    
    return list(answer.values())