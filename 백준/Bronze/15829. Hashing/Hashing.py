l = int(input()) # 문자열의 길이
strings = input() # 영문 소문자로 이뤄진 문자열

answer = 0
for i in range(l) :
    s = strings[i]
    answer += (ord(s) - 96) * (31**i)

print(answer % 1234567891)