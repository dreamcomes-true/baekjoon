import sys
input = sys.stdin.readline

hour, min = map(int, input().split())
time = int(input())

min = min + time
new_hour, new_min = min//60, min%60
hour += new_hour
min = new_min

if hour>23:
  hour -= 24

print(f'{hour} {min}')