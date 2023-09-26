answers = []
while True :
    nums = list(map(int, input().split()))
    nums.sort()
    a, b, c = nums
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if c**2 == a**2 + b**2 :
        answers.append("right")
    else :
        answers.append("wrong")

for i in answers:
    print(i)