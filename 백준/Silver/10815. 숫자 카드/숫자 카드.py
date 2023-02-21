import sys
input = sys.stdin.readline

n = int(input())
my_card = list(map(int, input().split()))

m = int(input())
keys = list(map(int, input().split()))

'''
n = 5
my_card = [6,3,2,10,-10]
m = 9
keys = [10,9,-5,2,3,4,5,-10]
'''
my_card.sort() # [2, 4, 5, 7, 8, 9, 11] , key = 9

def binary_search(lists, key):
  low, high = 0, len(lists)-1 # high = 7
  while low <= high :
    mid = (low+high)//2 # mid = (4+7)//2 = 5
    if lists[mid] < key :  # mid = 3, 7 < 9
      low = mid + 1 # low = 4. 
    elif lists[mid] > key :
      high = mid - 1
    else :
      return mid
  #while문을 빠져나온 경우는 키값이 없는 경우
  return None
      
answer = []
for i in keys :
  if binary_search(my_card, i) != None : 
    answer.append(1)
  else:
    answer.append(0)

for i in answer:
  print(i, end = ' ')
