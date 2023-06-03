def solution(operations):
    queue = []
    for operation in operations :
        op, num = operation.split()
        if op == "I" : 
            queue.append(int(num))
        elif queue == [] : 
            pass
        elif op == "D" and num == "1" :
            queue.remove(max(queue))
        else :
            queue.remove(min(queue))
    
    if queue == []: 
        return [0,0]
    else :
        return [max(queue), min(queue)]