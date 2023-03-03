def solution(phoneBook):    
    
    phoneBook.sort()
    for phone1, phone2 in zip(phoneBook, phoneBook[1:]):
        if phone2.startswith(phone1):
            return False
    return True
    
    
    
