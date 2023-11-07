n = int(input())
clap = ['3', '6', '9']

for num in range(1, n+1) :
    cnt = 0
    for i in str(num) :
        if i in clap : 
            cnt += 1
    if cnt == 0 : 
        print(num, end = ' ')
    else :
        print('-'*cnt, end = ' ')
        
