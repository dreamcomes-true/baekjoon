n = int(input())
numbers = []
for i in range(n):
  number = int(input())
  numbers.append(number)
numbers.sort()

for i in numbers:
  print(i)