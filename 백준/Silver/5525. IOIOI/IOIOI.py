n = int(input())
m = int(input()) # 문자열 s의 길이
s = input()

key = "IOI"+(n-1)*"OI"
n_key = len(key)
cnt = 0
for i in range(0, m - n_key + 1) :
    if s[i:i+n_key] == key :
        cnt += 1

print(cnt)
