strings = input()
explosion = input()


stack = []
n = len(explosion)
for i in strings:
    stack.append(i)
    if len(stack) >= n and "".join(stack[-n:]) == explosion :
        for _ in range(n):
            stack.pop()

if "".join(stack) == "" :
    print("FRULA")
else:
    print("".join(stack))