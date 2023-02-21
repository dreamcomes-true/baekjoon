import sys

n = int(sys.stdin.readline())

numbers = []

for i in range(n):
  numbers.append(int(sys.stdin.readline()))

numbers.sort()

for i in numbers:
  print(i)
