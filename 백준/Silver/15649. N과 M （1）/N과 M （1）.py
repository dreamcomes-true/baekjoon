import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

numlist = []


def dfs():
  
  if len(numlist) == m:
    print(' '.join(map(str, numlist)))
    return

  for i in range(1, n+1) : # 1부터 4에 대해서
    if i not in numlist : 
      numlist.append(i) # numlist = [1, 4]
      dfs()
      numlist.pop(-1) # [1]

dfs()