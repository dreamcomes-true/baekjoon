n, k = map(int, input().split())

people = [i+1 for i in range(n)]
order_list = []

idx = k - 1
while True :
    order_list.append(people[idx])
    people.pop(idx) 
    if len(people) == 0 :
        break
    if len(people) == 1 :
        order_list.append(people[0])
        break
    else :
        idx += (k-1)
        while idx >= len(people) :
            idx = idx - len(people) 

print("<" + ", ".join(list(map(str, order_list))).rstrip(", ")+">")