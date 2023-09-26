n = int(input())

people = []
for _ in range(n) :
    age, name = input().split()
    people.append([int(age), _, name])

people.sort(key= lambda x: (x[0], x[1]))

for person in people :
    print(person[0], person[2])