import re

def opening(name):
    f = open(name, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

def replacing(text):
    text = re.sub('(диноз(?:а|а́)вр(ы|(?:а(?:х|(?:ми?))?)|(?:о(?:в|м)?)|у|е)?)([^а-я])', 'кот\\2\\3', text)
    text = re.sub('(Диноз(?:а|а́)вр(ы|(?:а(?:х|(?:ми?))?)|(?:о(?:в|м)?)|у|е)?)([^а-я])', 'Кот\\2\\3', text)
    return text

def writing(name, text):
    f = open(name, 'w', encoding='utf-8')
    f.write(text)
    f.close()
        

text = opening('dino.htm')
text = replacing(text)
writing('kot.htm', text)
