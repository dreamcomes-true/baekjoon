def solution(sizes):
    max_list, min_list = [], []
    for size in sizes: 
        max_list.append(max(size))
        min_list.append(min(size))
    answer = max(max_list) * max(min_list)

    return answer