import re

def extract(name):
    f = open(name, 'r', encoding='utf-8')
    text = f.read().strip()
    f.close()
    words = text.split()
    for i in range(len(words)):
        words[i] = words[i].lower().strip(';.,^()[]?!:')
    return words       

def check(words):
    forms = []
    for word in words:
        if re.search("вып((и((л(а|о|и)?)|(т(ь|ая?|о(м|й|ю|е|(го))?|(ы(й|е|х|м)?)|ую)?)|(вш((и(й|е|х|ми?))|(ая)|е(е|(го)|й|(му)|ю|м)|(ую)))))|(ь((ют?)|(е(м|(шь)|те?))))|(ей(те)?))((ся)|(сь))?", word):
            forms.append(word)
    return (', ').join(forms)
    
def final():
    words = extract('2911.txt')
    checked = check(words)
    print(checked)

final()
