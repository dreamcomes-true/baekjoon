def moving_fish(new_list) :
    add_list = [[0] * len(new_list[i]) for i in range(len(new_list))]

    for x in range(len(new_list)):  # 각 리스트 (행) 에 대해서
        n = len(new_list[x])
        for y in range(n):  # 각 리스트의 (열) 에 대해서

            # 오른쪽과 차이 검사
            if y < n - 1:
                diff = new_list[x][y] - new_list[x][y + 1]
                fish_n = abs(diff) // 5  # 차이를 5로 나눈 몫이자, 보내야 하는 물고기 수
                if fish_n > 0:
                    if diff > 0:
                        add_list[x][y] -= fish_n
                        add_list[x][y + 1] += fish_n
                    else:
                        add_list[x][y] += fish_n
                        add_list[x][y + 1] -= fish_n

            # 아래 차이 검사
            if x < len(new_list) - 1:
                diff = new_list[x][y] - new_list[x + 1][y]
                fish_n = abs(diff) // 5  # 차이를 5로 나눈 몫이자, 보내야 하는 물고기 수
                if fish_n > 0:
                    if diff > 0:
                        add_list[x][y] -= fish_n
                        add_list[x + 1][y] += fish_n
                    else:
                        add_list[x][y] += fish_n
                        add_list[x + 1][y] -= fish_n

    for x in range(len(new_list)):  # 각 리스트 (행) 에 대해서
        n = len(new_list[x])
        for y in range(n):  # 각 리스트의 (열) 에 대해서
            new_list[x][y] += add_list[x][y]
    return new_list

def moving_in_line(new_list):
    back_list = []
    for i in range(len(new_list[0])):
        back_list += [x[i] for x in new_list][::-1]
    back_list += new_list[-1][len(new_list[0]):]
    return back_list


n, k = map(int, input().split()) # n = 어항수, k = 물고기 max값과 min값 차이 (목표)
fish = list(map(int, input().split()))
cnt = 0 # 어항정리 개수 카운트

# 어항정리 시작

while True :
    # 1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
    min_value = min(fish)
    for i, value in enumerate(fish) :
        if value == min_value :
            fish[i] += 1

    # 2. 어항 쌓기

    old_list = [[fish[0]], fish[1:]]

    while True :

        new_list = []
        for i in range(0, len(old_list[0])) :
            new_list.append([x[i] for x in old_list][::-1])
        new_list.append(old_list[-1][len(old_list[0]):])
        old_list = new_list

        if len(new_list) > len(new_list[-1]) - len(new_list[0]):
            break

    # 3. 물고기 수 조절 - 인접한 두 어항에 대해서, 물고기 수의 차이를 구한다
    new_list = moving_fish(new_list)

    # 4. 다시 일렬로 놓기
    back_list = moving_in_line(new_list)

    # 5. 다시 공중부양 (n/2개 공중부양 -> 두번 반복)
    new_list = []
    n = len(back_list)
    new_list.append(back_list[:n//2][::-1])
    new_list.append(back_list[n//2:])

    back_list = []
    back_list.append(new_list[-1][:n//4][::-1])
    back_list.append(new_list[0][:n//4][::-1])
    back_list.append(new_list[0][n//4:])
    back_list.append(new_list[-1][n//4:])

    # 6. 물고기 조절 다시 재수행
    new_list = moving_fish(back_list)

    # 7. 일렬 작업 재수행
    fish = moving_in_line(new_list)

    cnt += 1

    #  물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하인지 체크
    if max(fish) - min(fish) <= k :
        break

print(cnt)