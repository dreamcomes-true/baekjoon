from itertools import product
house_n = int(input())
costs = []
for i in range(house_n) :
    rgb = list(map(int, input().split()))
    costs.append(rgb)

dynamic_programming = [costs[0]]

for i in range(1, house_n) :
    red = costs[i][0] + min(dynamic_programming[i-1][1], dynamic_programming[i-1][2])
    green = costs[i][1] + min(dynamic_programming[i-1][0], dynamic_programming[i-1][2])
    blue = costs[i][2] + min(dynamic_programming[i-1][0], dynamic_programming[i-1][1])
    dynamic_programming.append([red, green, blue])

print(min(dynamic_programming[-1]))