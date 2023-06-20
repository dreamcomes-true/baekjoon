def solution(arr1, arr2):
    answer = []
    vertical_arr = [[] for i in range(len(arr2[0]))]
    for arr in arr2:
        for i in range(len(arr)):
            vertical_arr[i].append(arr[i])
    
    
    for i in range(len(arr1)) : 
            temp_list = []
            for j in range(len(vertical_arr)) : 
                element = [arr1[i][k]*vertical_arr[j][k] for k in range(len(arr1[0]))]
                temp_list.append(sum(element))
            answer.append(temp_list)
            
    return answer
