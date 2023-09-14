people_n, party_n = map(int, input().split()) # 사람 수, 파티 수
people_knows = list(map(int, input().split()))  # 진실 아는 사람들 배열 (첫 원소 = 사람수)
people_knows_n = people_knows[0]                # 진실을 아는 사람 수
if people_knows_n != 0 :
    people_knows = people_knows[1:]
else :
    people_knows = []
partys = []

for _ in range(party_n) :
    party = list(map(int, input().split()))[1:]
    partys.append(party)   

# people_knows 의 개수가 변동되지 않을 때까지 지속

while True :
    before_n = len(people_knows)
    for party in partys :
        if len(set(people_knows) & set(party)) > 0 :
            people_knows = list(set(people_knows) | set(party))
    if before_n == len(people_knows) :
        break

lie_count = 0
for party in partys :
    if len(set(people_knows) & set(party)) == 0 :
        lie_count += 1
print(lie_count)
