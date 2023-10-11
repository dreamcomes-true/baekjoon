n = int(input())
test_arr = []
answer = []
for _ in range(n) :
    test_arr.append(int(input()))

fibo_arr = [[1, 0], [0, 1], [1, 1]]
for test in test_arr :
    if test <= len(fibo_arr) -1 :
        answer.append(fibo_arr[test])
    else :
        i = len(fibo_arr)
        while i <= test :
            x1, y1 = fibo_arr[i-1]
            x2, y2 = fibo_arr[i-2]
            fibo_arr.append([x1+x2, y1+y2])
            i+=1
        answer.append(fibo_arr[test])

for ans in answer : 
    print(" ".join(list(map(str, ans))))