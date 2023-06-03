def solution(s):
    stack = []
    for i in range(len(s)) :
        if stack == [] : 
            stack.append(s[i])
        elif s[i] != stack[-1] : 
            stack.append(s[i])
        else :
            stack.pop(-1)
    if stack == [] :
        return 1
    else :
        return 0

# 시간초과 발생 코드
# def solution(s) :
#     pair_same = False
    
#     while True:
        
#         new_s = ""
#         pair_same = False
        
#         for i in range(len(s)):
#             if pair_same == True:
#                 pair_same = False
#             elif i == len(s)-1 : 
#                 new_s += s[i]
#             elif s[i] == s[i+1] :
#                 pair_same = True
#             else :
#                 new_s += s[i]
        
#         if new_s == "" :
#             return 1
#         elif new_s == s :
#             return 0
#         s = new_s[:]
    
