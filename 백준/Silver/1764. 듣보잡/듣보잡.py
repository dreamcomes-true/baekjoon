import sys
input = sys.stdin.readline

n, m = map(int, input().split())

hear = {}
answer = []

for i in range(n):
  temp = input().strip()
  hear[temp] = 1
  
for i in range(m):
  temp = input().strip()
  if hear.get(temp) != None:
    answer.append(temp)
    
answer.sort()
print(len(answer))
for i in answer:
  print(i)