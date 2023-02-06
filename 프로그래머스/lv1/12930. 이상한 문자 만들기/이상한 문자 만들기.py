def solution(s):
    answer = ''
    print(s)
    for word in s.split(' '): # ['try', 'hello', 'world']
        word = list(word) # ['t','r','y']
        print(word)
        trans_word = [word[i].upper() if i==0 or i%2 == 0 else word[i].lower() for i in range(len(word))]
        answer += "".join(trans_word) 
        answer += ' '
    return answer[:-1]

# trans_word = [i.upper() if word.index(i)%2==0 else i.lower() for i in list(word)]  # ['T', 'r', 'Y']
# => word.index(i)는 가장 먼저 찾은 글자의 인덱스를 반환하기 때문에 HeLLO가 출력되었음.