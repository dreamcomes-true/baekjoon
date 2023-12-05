n = int(input())

fibos = [0, 1]

for i in range(2, n+1) :
    fibos.append(fibos[i-1]+fibos[i-2])

print(fibos[-1])