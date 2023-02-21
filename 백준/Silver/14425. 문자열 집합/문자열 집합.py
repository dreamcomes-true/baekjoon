import sys
input = sys.stdin.readline

n, m = map(int, input().split())

S = []
cnt = 0
for i in range(n):
  S.append(input())
for i in range(m):
  temp = input()
  if temp in S:
    cnt+=1

print(cnt)