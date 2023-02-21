import sys
input = sys.stdin.readline

n = int(input())

people = []
winners = [1]*n

for i in range(n):
  people.append(list(map(int, input().split())))

#n = 5
#people = [[55,185],[58,183],[88,186],[60,175],[46,155]]


for i in range(n):
  for j in range(i+1, n):
    if people[i][0] > people[j][0] and people[i][1] > people[j][1] :
      winners[j] += 1
    elif people[i][0] < people[j][0] and people[i][1] < people[j][1] :
      winners[i] += 1

answer = ''
for ppl in winners :
  answer = answer + str(ppl) + ' '

print(answer[:-1])

  