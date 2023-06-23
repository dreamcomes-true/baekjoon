def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else :
                max_sum = max(triangle[i-1][j-1], triangle[i-1][j])
                triangle[i][j] += max_sum
    answer = max(triangle[len(triangle)-1])
            
    return answer