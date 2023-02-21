n = int(input())
numbers = list(map(int, input().split()))
minNum, maxNum = min(numbers), max(numbers)

print(str(minNum)+' '+str(maxNum))