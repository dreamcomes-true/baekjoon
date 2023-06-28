def solution(priorities, location):
    order = 1
    while priorities.index(max(priorities)) != location :
        max_index = priorities.index(max(priorities))
        priorities = priorities[max_index:] + priorities[:max_index]
        priorities.pop(0)
        
        if max_index < location : 
            location = location - max_index - 1
        else :
            location = location + len(priorities[max_index:]) 
        order += 1
        
    
        
    return order
'''
a b c d e f
1 1 9 1 1 1

c 
d e f a b
1 1 1 1 1

'''