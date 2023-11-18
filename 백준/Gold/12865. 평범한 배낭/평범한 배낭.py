
numbers, max_weight = map(int, input().split())

weights, values = [], []
for i in range(numbers) :
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

dynamic_program = [[0 for kilogram in range(max_weight+1)] for nums in range(numbers+1)]

for i in range(1, numbers+1) : # i = 물건 넘버
    for kilo in range(0, max_weight+1) : # 0부터 k까지 무게에 대하여
        # 만약 현재 최대무게 kilo보다 해당 물건의 무게가 더 무겁다면 ? -> 포함 x
        if kilo < weights[i-1] :
            dynamic_program[i][kilo] = dynamic_program[i-1][kilo]
        else :
            dynamic_program[i][kilo] = max(dynamic_program[i-1][kilo], dynamic_program[i-1][kilo-weights[i-1]] + values[i-1])
            # 현재 물건을 포함 안하는 경우 = dynamic_program[i-1][kilo]
            # 현재 물건을 포함하는 경우 = dynamic_program[i-1][kilo-weights[i]] + values[i]

print(dynamic_program[-1][-1])