weight = int(input())
answer = -1

a = weight // 5
b = ( weight % 5 ) // 3
left = ( weight % 5 ) % 3

while True:
    if left == 0 :
        answer = a + b
        break
    elif a == 0 and left != 0 :
        break
    else :
        a -= 1
        b = ( weight - 5 * a ) // 3
        left = ( weight - 5 * a ) % 3

print(answer)