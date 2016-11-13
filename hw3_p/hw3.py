latin = 'qwertyuiopasdfghjklzxcvbnm '
x = True
endings = ['re', 'ri']
analytism = ['esse', 'iri']
words = []
while True:
    word = input('Введите латинское слово: ')
    if word == '':
        break
    else:
        for l in word:
            if l not in latin:
                x = False
                print('Слово не латинское. Введите другое слово.')
                break
        if x == True:
            words.append(word)
for w in words:
    if ' ' in w:
        w_split = w.split()
        if w_split[1] in analytism:
            print(w, ' - инфинитив.')
    else:
        if w[len(w)-2::] in endings or w[len(w)-4::] == 'isse':
            print(w, ' - инфинитив.')
        
        
        
        
