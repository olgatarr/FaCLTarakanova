word = input('Введите слово: ') 
for i in range(len(word)): 
    print(word) 
    newword = word[len(word)-1] + word[0:len(word)-1] 
    word = newword 
    newword = ''
