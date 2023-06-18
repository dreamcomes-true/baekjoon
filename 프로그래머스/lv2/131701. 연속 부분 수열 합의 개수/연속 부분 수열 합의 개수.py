def solution(elements):
    circle_elements = elements + elements # [7,9,1,1,4,7,9,1,1,4]
    answer_list = []
    for n in range(1, len(elements)): # len = 1개 ~ 4개일 때
        for i in range(len(elements)) : 
            answer_list.append(sum(circle_elements[i:i+n]))
    answer_list.append(sum(elements))
    
    return len(set(answer_list))

