from itertools import permutations

def is_num(num): # 소수이지 판별하는 함수
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    n_list = [i for i in numbers]
    answers = []
    
    for n in range(1, len(n_list)+1) : # 숫자가 1개인 경우부터 3개인 경우까지
        for i in permutations(n_list, n) : 
            answers.append(int(''.join(list(i))))
    
    answer = list(set(answers))
    final_answer = []
    for num in answer : 
        if num != 1 and num != 0 and is_num(num) == True:
            final_answer.append(num)
    
    
    '''
    숫자의 개수가 1인 경우 : 1
    숫자의 개수가 2개인 경우
    1) 1자리 숫자 : a, b
    2) 2자리 숫자 : ab, ba
    숫자의 개수가 3개인 경우
    1) 1자리 숫자 : a, b, c
    2) 2자리 숫자 : ab, ba, cb, bc, ac, ca
    3) 3자리 숫자 : abc, acb, bac, bca, cab, cba
    
    
    '''
    return len(final_answer)