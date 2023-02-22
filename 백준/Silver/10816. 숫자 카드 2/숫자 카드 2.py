import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cnt = Counter(cards) # counter 생성 {'6':2, '3':2 ..}

m = int(input())
checkNums = list(map(int, input().split()))

'''
n = 10
m = 8
cards = [6,3,2,10,10,10,-10,-10,7,3]
checkNums = [10,9,-5,2,3,4,5,-10]
cnt = Counter(cards) # counter 생성 {'6':2, '3':2 ..}
'''

answer = []
for i in range(m):
  key = checkNums[i]
  check = cnt[key]
  answer.append(check)
  
for i in answer :
  print(i, end=' ')