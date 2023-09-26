a, b = map(int, input().split())
original_a, original_b = a, b
if a < b :
    a, b = b, a

while True :
    a, b = b, a%b
    if b == 0 :
        break


print(a)
print(a * (original_a//a) * (original_b//a))