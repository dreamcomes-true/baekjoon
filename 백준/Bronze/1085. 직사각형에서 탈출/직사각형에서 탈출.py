import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

# (x, y)에서 x=0까지 거리 / y=0까지 거리 / x = w까지 거리 / y = h 까지 거리를 구한다

dist = [abs(x), abs(y), abs(w-x), abs(h-y)]
print(min(dist))