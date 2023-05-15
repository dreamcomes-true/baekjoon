def solution(s):
    queue = []
    for i in s :
        if i == '(' :
            queue.append(i)
        else :
            if queue == []:
                return False
            else :
                queue.pop()
    if queue == [] :
        return True
    else :
        return False
    