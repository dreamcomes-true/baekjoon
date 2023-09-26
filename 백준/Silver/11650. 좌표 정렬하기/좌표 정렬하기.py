n = int(input())

coordinates = []
for _ in range(n) :
    x, y = map(int, input().split())
    coordinates.append([x,y])

coordinates.sort(key=lambda x: (x[0], x[1]))

for dots in coordinates :
    print(dots[0], dots[1])