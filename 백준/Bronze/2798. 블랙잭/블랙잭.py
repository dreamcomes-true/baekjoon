card_n, sum_limit = map(int, input().split())
cards = list(map(int, input().split()))
#card_n, sum_limit = 5, 21
#cards = [5,6,7,8,9]
max = 0

for i in range(card_n):
  # 시작 수 = i
  for j in range(i+1, card_n):
    # 두번째 수 = j
    for l in range(j+1, card_n):
      # 세번째 수 = l
      sum = cards[i]+ cards[j] + cards[l]
      if sum <= sum_limit and sum > max :
        max = sum
print(max)
