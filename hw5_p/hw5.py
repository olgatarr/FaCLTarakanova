f = open('2911.txt', 'r', encoding='utf-8')
signs = '.,:;?!'
lines = f.read()
words = lines.split(' ')
counter = 0
counter_with = 0
for word in words:
    if len(word) > 10:
        counter_with += 1
    if word[-1] not in signs:
        if len(word) > 10:
            counter += 1
    else:
        if len(word[:len(word)-1:]) < 10:
            counter += 1
print(counter/len(words), ' - доля слов длиннее 10 символов (без знаков препинания)')
print(counter_with/len(words),  ' - доля слов длиннее 10 символов (знаки препинания как часть слов)')
f.close()
