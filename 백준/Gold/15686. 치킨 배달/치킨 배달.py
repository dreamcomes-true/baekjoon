from itertools import combinations

n, m = map(int, input().split())
city = []
for i in range(n) :
    temp_city = list(map(int, input().split()))
    city.append(temp_city)

chicken_nums = 0
chicken_location = []
home_nums = 0
home_location = []
for i in range(n):
    for j in range(n) :
        if city[i][j] == 2:
            chicken_nums += 1 
            chicken_location.append((i, j))
        elif city[i][j] == 1:
            home_nums += 1
            home_location.append((i, j))
remove_num = chicken_nums - m


def calculating_chicken_dist(home_location, chicken_location) :
    temp_dist = 0
    for (x, y) in home_location:
        if (x, y-1)  in chicken_location or (x, y+1)  in chicken_location or (x-1, y)  in chicken_location or (x+1, y) in chicken_location:
            temp_dist += 1
        elif (x, y-2)  in chicken_location or (x, y+2)  in chicken_location or (x-2, y)  in chicken_location or (x+2, y)  in chicken_location or (x-1, y-1)  in chicken_location or (x+1,y+1)  in chicken_location or (x-1, y+1)  in chicken_location or (x+1, y-1) in chicken_location :
            temp_dist += 2
        else :
            min_dist = -1
            for i in chicken_location:
                if min_dist < 0 :
                    min_dist = abs(i[0]-x) + abs(i[1]-y)#
                elif min_dist > abs(i[0]-x) + abs(i[1]-y) :
                    min_dist = abs(i[0]-x) + abs(i[1]-y)
            temp_dist += min_dist
    return temp_dist

if remove_num == 0:
    dist = calculating_chicken_dist(home_location, chicken_location)
    print(dist)
else:
    remove_list = list(combinations(chicken_location, remove_num))

    dist = []
    for removals in remove_list:
        temp_dist = 0
        temp_chicken = chicken_location.copy()
        for i in removals:
            temp_chicken.remove((i[0], i[1]))
            
        temp_dist = calculating_chicken_dist(home_location, temp_chicken)
        dist.append(temp_dist)
    print(min(dist))