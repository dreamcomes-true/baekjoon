import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n) :
    order = input().split()
    if order[0] == 'empty' :
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == 'back' :
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'pop_front': 
        if len(queue) == 0:
            print(-1)
        else:
            first = queue.popleft()
            print(first)
    elif order[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            back = queue.pop()
            print(back)
    elif order[0] == 'push_back' :
        num = int(order[1])
        queue.append(num)
    else :
        num = int(order[1])
        queue.appendleft(num)