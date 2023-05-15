def solution(s) :
    s = s.split(" ") 
    answer = []
    for word in s :
        if word : 
            k = word[0].upper() + word[1:].lower()
            answer.append(k)
        else :
            answer.append(word)
    return " ".join(answer)


