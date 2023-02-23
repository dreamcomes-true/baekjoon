import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

adj_list = [[] for i in range(n+1)]
# 정점 0부터 n까지의 인접 리스트
visited = [0 for i in range(n+1)]
# 방문 순서에 대한 리스트

for i in range(m) :
  x, y = map(int, input().split())
  adj_list[x].append(y)
  adj_list[y].append(x)

for i in range(n+1):
  adj_list[i].sort()

order = 0 # 순서 기록을 위한 변수

def dfs(i):
  if visited[i] == 0:
    global order
    order += 1
    visited[i] = order
    for j in adj_list[i] :
      dfs(j)
  else:
    pass
    
dfs(r)

for i in range(1, n+1):
  print(visited[i])