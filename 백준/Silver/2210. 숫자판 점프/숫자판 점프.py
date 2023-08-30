number_plates = []
for i in range(5):
    number_plates.append(list(map(int, input().split())))

answer = []

def dfs(x, y, num) : # [0, 0, 1]
    
    adj_list = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

    for i in adj_list :
        
        if len(num) == 5 :
            if i[0] >= 0 and i[0] < 5 and i[1] >= 0 and i[1] < 5 :
                answer.append(num + str(number_plates[i[0]][i[1]]))
        else :
            if i[0] >= 0 and i[0] < 5 and i[1] >= 0 and i[1] < 5 :
              dfs(i[0], i[1], num + str(number_plates[i[0]][i[1]])) 

    return


for x in range(5) :
    for y in range(5) :
        # 모든 위치에서 한번씩 시작해 볼 수 있도록 한다
        # 임의의 위치에서
        selected_num = str(number_plates[x][y])
        
        dfs(x, y, selected_num) # 1
    
print(len(set(answer)))