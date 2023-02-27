n, m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

common = n + m-len(list(set(a+b))) # 공통 개수 
print(n + m - common * 2)