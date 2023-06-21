def solution(s):
    
    s = s[1:-1]
    is_n = False
    total = []
    queue = []
    n_string = ""
    for i in range(len(s)) :
        if s[i] == "{":
            is_n = True
        elif s[i] == "}":
            is_n = False
            total.append(queue)
            queue = []
        elif is_n == True:
            '''
            4, 2, 3
            13, 2, 33
            , 인 경우 
            '''
            if s[i] != "," and s[i+1] not in [",", "}"] : # 숫자인데 뒤에도 숫자인 경우
                n_string += s[i]
            elif s[i] != "," and s[i+1] in [",", "}"] : # 숫자인데 뒤에 , 인 경우
                if n_string == "" :
                    queue.append(int(s[i]))
                else :
                    n_string += s[i]
                    queue.append(int(n_string))
                    n_string = ""
                    
    total.sort(key = lambda x : len(x))
    
    answer = []
    for arr in total :
        for j in arr :
            if j not in answer:
                answer.append(j)
    
    return answer
        