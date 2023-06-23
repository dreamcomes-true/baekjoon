import heapq

def solution(n, works):
    
    
    if n >= sum(works) :
        return 0
    
    works = [(-1)*i for i in works]
    
    heapq.heapify(works)
    
    while n != 0:
        max_n = heapq.heappop(works)
        heapq.heappush(works, max_n+1)
        n -=1
    
    answer =0
    for i in works :
        answer += i*i
        
    return answer