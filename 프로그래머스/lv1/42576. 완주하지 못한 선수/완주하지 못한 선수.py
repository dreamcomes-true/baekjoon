def solution(participant, completion):
    athlete = dict()
    for parti in participant:
        if parti in athlete.keys():
            athlete[parti] += 1
        else:
            athlete[parti] = 1
    for parti in completion :
        if athlete[parti] == 1 :
            del athlete[parti]
        else:
            athlete[parti] -= 1
    
    for i in athlete.keys():
        answer = i
    

    return answer