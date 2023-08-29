numbers = int(input())

for n in range(numbers) :
    parenthesis = input()
    p_stack = []
    is_vps = True
    for i in parenthesis:
        if i == '(' :
            p_stack.append(i)
        else :
            if p_stack == []:
                is_vps = False
                break
            else :
                p_stack.pop(-1)
    if p_stack == [] and is_vps == True :
        print('YES')
    else :
        print('NO')
