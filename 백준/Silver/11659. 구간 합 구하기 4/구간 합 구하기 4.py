import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = []
total = 0

for num in num_list : # 최대 10만번 수행
    total += num
    sum_list.append(total)

for i in range(m) :
    start, end = map(int, input().split())
    if start == 1 :
        print(sum_list[end-1])
    else :
        print(sum_list[end-1] - sum_list[start-2])  # 인덱스 i에 대한 리스트 인덱싱 = O(1)

