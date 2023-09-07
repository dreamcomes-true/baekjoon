n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
num_list.sort()

def gcd(a, b) :
    if b > a :
        a, b = b, a
    while b > 0 :
        a, b = b, a % b
    return a

gcd_n = num_list[1]-num_list[0]
for i in range(1, len(num_list)-1): 
    gcd_n = gcd(gcd_n, num_list[i+1]-num_list[i])

answer = []
for i in range(1, int(gcd_n**0.5)+1) :
    if gcd_n % i == 0 :
        answer.append(i)
        if i != gcd_n // i :
            answer.append(gcd_n//i)
answer.remove(1)
answer.sort()

returnvalue = " ".join(map(str, answer))
print(returnvalue)