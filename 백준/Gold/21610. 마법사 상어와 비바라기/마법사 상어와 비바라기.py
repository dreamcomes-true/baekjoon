

n, m = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(n)]
orders = [list(map(int, input().split())) for _ in range(m)]
clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]  # 현재 구름의 위치를 담는 배열
directions = { 1: (0, -1), 2: (-1,-1), 3: (-1, 0), 4: (-1, 1),
               5: (0, 1),  6: (1, 1),  7: (1, 0),  8: (1, -1) }
cross = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # 대각선 위치 차이

for direct, dist in orders : # i번째 명령어
    dx, dy = directions[direct] # 이동할 x 거리와 y 거리
    moved_clouds = set()

    # 구름 이동 -> 구름 위치 업데이트
    for x, y in clouds : # c 번째 구름에 대해서

        x = (x + dist * dx) % n
        y = (y + dist * dy) % n

        moved_clouds.add((x, y))
        water[x][y] += 1    # 이동한 구름 위치에 비가 1씩 내림

    for x, y in moved_clouds:  # c 번째 구름에 대해서
        # 대각선 위치에 물이 있는 개수 체크
        cnt = 0
        for dx, dy in cross :
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1 :
                if water[nx][ny] > 0 :
                    cnt += 1
        water[x][y] += cnt

    # 물의 양이 2 이상인 구름 찾기
    new_clouds = []
    for x in range(n) :
        for y in range(n) :
            if (x, y) not in moved_clouds and water[x][y] >= 2 :
                new_clouds.append([x, y])
                water[x][y] -= 2
    clouds = new_clouds

print(sum([sum(i) for i in water]))
