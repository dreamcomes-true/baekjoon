test_n = int(input())

for i in range(test_n) :
    n, m = map(int, input().split())
    n, m = min(n, m), max(n, m)
    
    dynamic_programming = [[], [i for i in range(m+1)]]

    for i in range(2, n+1) :
        dynamic_programming.append([0] * (i))
        dynamic_programming[-1].append(1)
        for j in range(i+1, m+1) :
            dynamic_programming[-1].append(sum(dynamic_programming[-2][i-1:j]))

    print(dynamic_programming[-1][-1])