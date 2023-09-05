S = input()
T = input()

is_possible = False
string_list = [T]

while True:

    new_string_list = []
    for strings in string_list :

        if strings[-1] == 'A' :
            temp_string = strings[:-1]
        else :
            strings = strings[:-1]
            temp_string = strings[::-1]

        if temp_string == S :
            is_possible = True
            break
        elif len(temp_string) >= len(S) :
                new_string_list.append(temp_string)
    if new_string_list == [] or is_possible == True :
        break
    string_list = new_string_list.copy()
    
if is_possible == True:
    print(1)
else:
    print(0)

    