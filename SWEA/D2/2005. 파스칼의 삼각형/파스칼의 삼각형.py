def pascalTriangle(n) :
    triangle = [[1]]
    now = 1
    while (now < n) :
        before = triangle[-1] # [1, 2, 1]
        now += 1 # 현재 만드는 줄이 몇번째인지 (4번째)
        after = []
        for idx in range(now) : # 4
            if idx == 0 or idx == now-1 :
                after.append(1)
            else :
                after.append(before[idx] + before[idx-1])
        triangle.append(after)
    for tri in triangle :
        tri_str = list(map(str, tri))
        print(" ".join(tri_str))


testcaseNumber = int(input())

for i in range(testcaseNumber) :
    n = int(input())
    print(f'#{i+1}')
    pascalTriangle(n)
