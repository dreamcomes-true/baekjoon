testcase_num = int(input())
testcase = []

for i in range(testcase_num) :
    temp_function = input()
    n = int(input())
    if n == 1:
        temp_arr = [(int(input()[1:-1]))]
    elif n == 0 : 
        temp_arr = input()
        temp_arr = []
    else :
        temp_arr = list(map(int, input()[1:-1].split(',')))
    testcase.append([temp_function, n, temp_arr])

for case in testcase :
    is_error = False
    function, n, arr = case
    cnt = 0
    for order in function :
        if order == 'R' :
            cnt += 1
        elif order == 'D' :
            if arr == [] :
                is_error = True
                break
            elif cnt %2 == 0 :
                arr.pop(0)
            else :
                arr.pop(-1)
    if is_error : 
        print("error")
    else:
        if cnt % 2 == 0:
            print("["+",".join(map(str, arr))+"]")
        else :
            arr.reverse()
            print("["+",".join(map(str, arr))+"]")