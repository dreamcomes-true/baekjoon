import sys
input = sys.stdin.readline

n = int(input())
numbers = [0]*10001 # 0부터 10000까지의 리스트

for i in range(n):
  temp = int(input())
  numbers[temp] += 1

for i in range(10001):
  if numbers[i] != 0:
    for j in range(numbers[i]):
      print(i)