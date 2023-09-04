from itertools import combinations

l, c = map(int, input().split())
word_list = list(input().split())

combi_list = combinations(word_list, l)


consonant = ['a', 'e', 'i', 'o', 'u']

passwords = []
for words in combi_list:
    consonant_true = False
    vowel_true = True
    words = list(words)
    words.sort()
    temp_word = words.copy()
    for i in consonant:
        if i in words: 
            consonant_true = True
            temp_word.remove(i)
    if len(temp_word) < 2 :
        vowel_true = False
    if consonant_true == True and vowel_true == True :
        passwords.append("".join(words))

passwords.sort()
for i in passwords :
    print(i)