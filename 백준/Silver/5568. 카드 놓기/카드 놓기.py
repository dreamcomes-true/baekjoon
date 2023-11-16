from itertools import permutations


n = int(input())    # 카드가 총 n장
k = int(input())    # 선택할 카드는 k장
cards = []
for _ in range(n) :
    cards.append(input())
total_cases = permutations(cards, k)
answer = []
for case in total_cases :
    answer.append("".join(case))
answer = set(list(map(int, answer)))
print(len(answer))