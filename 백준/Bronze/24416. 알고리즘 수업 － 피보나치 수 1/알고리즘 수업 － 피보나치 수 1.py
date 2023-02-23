import sys

input = sys.stdin.readline
num = int(input())

cnt1 = 0

def fibo1(n) :
  if n == 1 or n == 2 :
    global cnt1
    cnt1 += 1
    return 1
  else :
    return fibo1(n-1) + fibo1(n-2)

f = [0]*num
cnt2 = 0
def fibo2(n) :
  f[0], f[1] = 1, 1
  for i in range(2, n) :
    global cnt2
    cnt2 += 1
    f[i] = f[i-1] + f[i-2]
  return f[n-1]

f1 = fibo1(num)
f2 = fibo2(num)
print(f'{cnt1} {cnt2}')