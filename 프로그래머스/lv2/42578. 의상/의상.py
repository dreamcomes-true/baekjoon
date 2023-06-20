def solution(clothes):
    clothes_dict = {}
    cnt = 1
    for cloth in clothes :
        if cloth[1] in clothes_dict.keys() :
            clothes_dict[cloth[1]]+= 1
        else:
            clothes_dict[cloth[1]] = 1
    for i in list(clothes_dict.values()) :
        cnt *= (i+1)
    return cnt -1
