a, b, c = map(int, input().split())


def calculate(a, b) :
    if b == 1 :
        return a % c
    if b % 2 == 0:
        return (calculate(a, b//2) ** 2) % c
    else :
        return (calculate(a, b//2) * calculate(a, b//2+1)) % c

answer = calculate(a, b)
print(answer)