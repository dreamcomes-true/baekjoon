from collections import deque

n = int(input())
orders = []
for _ in range(n) :
    orders.append(input())

queue = deque([])
answers = []
for order in orders :
    if order == 'size':
        answers.append(len(queue))
    elif order == 'empty':
        if len(queue) == 0 :
            answers.append(1)
        else:
            answers.append(0)
    elif order == 'front':
        if len(queue) == 0 :
            answers.append(-1)
        else :
            answers.append(queue[0])
    elif order == 'back':
        if len(queue) == 0 :
            answers.append(-1)
        else :
            answers.append(queue[-1])
    elif order == 'pop':
        if len(queue) == 0 :
            answers.append(-1)
        else :
            first = queue.popleft()
            answers.append(first)
    else :
        queue.append(int(order[5:]))

for i in answers :
    print(i)