a, b, c = map(int, input().split())
#a, b, c = 5, 8, 4
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)