def check_palindrome(name) :
    name_stack = []
   
    if name == name[::-1] :
      return 0

    else :
      is_pseudo = False
      k = len(name) - 1 
      for i in range(len(name)) :
        if i >= k :
           break
        if name[i] == name[k] :
            k -= 1
            pass
        else:
            temp_name = name[:i] + name[i+1:]
            if temp_name == temp_name[::-1]:
               is_pseudo = True
               break
            else :
               temp_name = name[:k] + name[k+1:]
               if temp_name == temp_name[::-1] :
                is_pseudo = True
               break
      if is_pseudo == True :
         return 1
      else :
         return 2

n = int(input())
str_list = []

for i in range(n) :
    str_list.append(input())

for str in str_list :
    print(check_palindrome(str))
