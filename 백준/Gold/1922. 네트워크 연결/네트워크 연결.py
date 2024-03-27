def find_parent(parent, i) :
  if i == parent[i] :
    return i
  else :
    parent[i] = find_parent(parent, parent[i])
  return parent[i]


def kruskal(computers) :
  total = 0
  cnt = 0
  computers.sort(key = lambda x:x[2])

  for a, b, cost in computers :
      root_a = find_parent(parent, a)
      root_b = find_parent(parent, b)

      if root_a != root_b :
        cnt += 1
        total += cost
        if rank[a] == rank[b] :
          parent[root_a] = root_b
          rank[b] += 1
        elif rank[a] > rank[b] :
          parent[root_b] = root_a
        else :
          parent[root_a] = root_b

      if cnt == n -1 :
        break
  return total


n = int(input())
m = int(input())
computers = []
for _ in range(m) :
  a, b, cost = map(int, input().split())
  computers.append([a, b, cost])

parent = [i for i in range(0, n+1)]
rank = [0 for i in range(0, n+1)]
min_cost = kruskal(computers)
print(min_cost)