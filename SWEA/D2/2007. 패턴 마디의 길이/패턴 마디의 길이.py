def find_string_length(words) :
    answer = 0
    for i in range(1, 11) :
        length = 30 // i
        if 30 % i == 0 :
            if words[0:i] * length == words :
                answer = i
                break
        else :
            if words[0:i] * length == words[0:length*i] :
            	answer = i
            	break
    return answer

n = int(input())
testcases = []
for i in range(n) :
    answer = find_string_length(input())
    print(f'#{i+1} {answer}')
    
