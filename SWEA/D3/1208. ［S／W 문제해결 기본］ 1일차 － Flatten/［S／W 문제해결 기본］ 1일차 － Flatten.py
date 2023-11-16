def findHeightDiff(dumpNumber, boxes) :
    for i in range(dumpNumber) : # 총 덤프 횟수만큼 반복
        maxHeight = max(boxes)
        maxIndex = boxes.index(maxHeight)
        minHeight = min(boxes)
        minIndex = boxes.index(minHeight)

        boxes[maxIndex] -= 1
        boxes[minIndex] += 1

    return max(boxes) - min(boxes)





for i in range(10) :
    dumpNumber = int(input())
    boxes = list(map(int, input().split()))
    diff = findHeightDiff(dumpNumber, boxes)
    print(f'#{i+1} {diff}')