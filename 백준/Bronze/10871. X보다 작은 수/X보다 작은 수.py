n, x = map(int, input().split())
numbers = list(map(int, input().split()))
answer = ''
for i in numbers:
  if i < x:
    answer = answer + str(i) + ' '

print(answer[:-1])