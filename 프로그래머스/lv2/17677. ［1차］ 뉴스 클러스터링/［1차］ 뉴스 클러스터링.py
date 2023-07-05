def check_str(string) :
    string = string.upper()
    answer = []
    part_string = ''
    
    for i in string:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            part_string += i
        else :
            if part_string != '':
                answer.append(part_string)
            part_string = ''
    if part_string != '':
                answer.append(part_string)
    
    return answer

def slicing(string) :
    n = len(string)
    answer = []
    for i in range(n-1) : # 0부터 n-1까지
        answer.append(string[i:i+2])
    return answer

def making_dict(list) :
    list_dict = {}
    for i in list :
        if i not in list_dict.keys() :
            list_dict[i] = 1
        else :
            list_dict[i] += 1
    return list_dict

def similiarity(dict1, dict2) :
    union = 0
    diff = 0
    for i in dict1.keys():
        if i in dict2.keys() :
            diff += min(dict1[i], dict2[i])
            union += max(dict1[i], dict2[i])
            del dict2[i]
        else :
            union += dict1[i]
    union += sum(dict2.values())
    
    return (diff/union) * 65536
            
    '''
    1 : 2개, 2 : 2개, 3 : 1개
    1 : 1개, 2 : 2개, 4 : 1개, 5 : 1개
    -> 1 교집합 1개, 2 교집합 2개 -> 총 교집합 3개
    -> 1 2개, 2 2개, 3 1개, 4 1개, 5 1개 => 7개
    '''
    
        
            
def solution(str1, str2):
    answer = 0
    str1 = check_str(str1)
    str2 = check_str(str2)
    
    print(str1, str2)
    str1_list, str2_list = [], []
    for part in str1 :
        str1_list += slicing(part)
    for part in str2 :
        str2_list += slicing(part)
    
    if str1_list == [] and str2_list == [] :
        answer = 65536
    else :
        list1_dict = making_dict(str1_list)
        list2_dict = making_dict(str2_list)
        answer = similiarity(list1_dict, list2_dict)
    
    return int(answer)