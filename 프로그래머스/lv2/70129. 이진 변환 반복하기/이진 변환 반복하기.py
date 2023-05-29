def solution(s):
    cnt_remove = 0
    cnt_loop = 0
    while True:
        if s == '1' : break
        cnt_loop += 1
        before = len(s)
        s = s.replace('0', "")
        after = len(s)
        s = bin(after)[2:]
        cnt_remove += (before - after)
        
    return [cnt_loop, cnt_remove]