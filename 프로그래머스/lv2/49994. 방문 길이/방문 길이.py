def solution(dirs):
    # status = [0,0,1,1]
    # road = [[0,0,0,0],[0,0,1,0] ~]
    '''
    "UDU" 의 경우, 1이 나와야합니다.
    아마 가는 경로와 되돌아오는 경로를 다른 경로라고 생각하셔서 그럴거에요.
    '''
    road = [[0,0,0,0]]
    cnt = 0
    for dir in dirs :
        if dir == 'U':
            status = [road[-1][2], road[-1][3], road[-1][2], road[-1][3]+1]
            status2 = [road[-1][2], road[-1][3]+1, road[-1][2], road[-1][3]]
            if status in road or status2 in road: # 거쳐간 길이면
                cnt += 1
            if status[2] < -5 or status[2]>5 or status[3]<-5 or status[3]>5 :
                cnt += 1
            else :
                road.append(status)
        elif dir == 'L':
            status = [road[-1][2], road[-1][3], road[-1][2]-1, road[-1][3]]
            status2 = [road[-1][2]-1, road[-1][3], road[-1][2], road[-1][3]]
            if status in road or status2 in road: # 거쳐간 길이면
                cnt += 1
            if status[2] < -5 or status[2]>5 or status[3]<-5 or status[3]>5 :
                cnt += 1
            else :
                road.append(status)
        elif dir == 'R':
            status = [road[-1][2], road[-1][3], road[-1][2]+1, road[-1][3]]
            status2 = [road[-1][2]+1, road[-1][3], road[-1][2], road[-1][3]]
            if status in road or status2 in road: # 거쳐간 길이면
                cnt += 1
            if status[2] < -5 or status[2]>5 or status[3]<-5 or status[3]>5 :
                cnt += 1
            else :
                road.append(status)
        else:
            status = [road[-1][2], road[-1][3], road[-1][2], road[-1][3]-1]
            status2 = [road[-1][2], road[-1][3]-1, road[-1][2], road[-1][3]]
            if status in road or status2 in road: # 거쳐간 길이면
                cnt += 1
            if status[2] < -5 or status[2]>5 or status[3]<-5 or status[3]>5 :
                cnt += 1
            else :
                road.append(status)

    return len(dirs) - cnt