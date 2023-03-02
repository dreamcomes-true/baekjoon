def solution(answers):
    cnt1, cnt2, cnt3 = 0,0,0
    answer1 = [1, 2, 3, 4, 5]*(len(answers)//5+1)
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5]*(len(answers)//8+1)
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(len(answers)//10+1)

    for i in range(len(answers)):
        if (answers[i] == answer1[i]) : 
            cnt1 += 1
        if (answers[i] == answer2[i]) : 
            cnt2 += 1
        if (answers[i] == answer3[i]) :
            cnt3 += 1
    answer = []
    
    if cnt1 == max([cnt1,cnt2,cnt3]) :
        answer.append(1)
    if cnt2 == max([cnt1,cnt2,cnt3]) :
        answer.append(2)
    if cnt3 == max([cnt1,cnt2,cnt3]) :
        answer.append(3)
    answer.sort()
    
    return answer