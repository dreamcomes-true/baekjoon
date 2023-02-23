import sys
input = sys.stdin.readline

n = int(input())
    
stack = []
answer = []
for i in range(n):
  order = input().strip()
  if order[:4] == 'push' :
    ord, num = order.split()
    stack.append(int(num))
  elif order == 'pop' :
    if len(stack) == 0:
      #print(-1)
      answer.append(-1)
    else: 
      num = stack.pop(-1) # 맞는지 확인
      #print(num)
      answer.append(num)
  elif order == 'size' :
    #print(len(stack))
    answer.append(len(stack))
  elif order == 'empty' :
    if len(stack) == 0:
      #print(1)  
      answer.append(1)
    else:
      #print(0)
      answer.append(0)
  elif order == 'top' :
    if len(stack) == 0:
      #print(-1)
      answer.append(-1)
    else:
      #print(stack[-1])
      answer.append(stack[-1])



for i in answer:
  print(i)