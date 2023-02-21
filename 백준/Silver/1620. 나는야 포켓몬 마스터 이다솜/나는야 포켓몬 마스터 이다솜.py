import sys
input = sys.stdin.readline


n, m = map(int, input().split())

poketmon = {}
for i in range(1, n+1):
  poketmon[i] = input().strip()

poketmon2 = {value:key for key, value in poketmon.items()}

answer = []
for i in range(m):
  key = input().strip()
  if key.isdigit(): # 숫자인 경우
    answer.append(poketmon.get(int(key)))
  else : # 포켓몬 이름인 경우
    answer.append(poketmon2.get(key))

for i in range(m):
  print(answer[i])