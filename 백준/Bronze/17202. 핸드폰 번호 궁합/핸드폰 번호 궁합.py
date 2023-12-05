first = input()
second = input()

number = ''
for i in range(8) :
    number += first[i]
    number += second[i]

while len(number) > 2:
    answer = ''
    for i in range(len(number) -1):
        temp_sum = int(number[i]) + int(number[i+1])
        answer += str(temp_sum % 10)
    number = answer

print(number)