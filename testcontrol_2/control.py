import re
import csv

def opening(name):
    f = open(name, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    text = text.strip()
    text = text.replace("— ", "")
    return text

def splitting(text):
    words = []
    words = text.split()
    return words

def counting(words):
    for i in range(len(words)):
        words[i] = words[i].strip('....,?*()«»!\'\":; ').lower()
    words = sorted(words)
    return words

def freq(words):
    dic = {}
    for word in words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    with open('freq.csv', 'w', encoding='utf-8') as f: ##8
        output = csv.writer(f, delimiter=',')
        header = ['слово', 'частота']
        output.writerow(header)
        for key in dic:
            output.writerow([key, dic[key]])
    return dic

def final():
    text = opening('text.txt')
    words = splitting(text)
    words = counting(words)
    dic = freq(words)
    agos = re.findall('(?:(?:[А-Яа-яіѢѣ])+[\s,.!\?:;"\(\)\'»\n\t—]+?){3}[А-Яа-яiѢѣ]+?аго [А-Яа-яiѢѣ]+?(?:а|и)[\s,.!\?:;"\(\)\'»\n\t—]{,5}(?:[А-Яа-яiѢѣ]+?[\s,.!\?;:—"\(\)\'»\n\t]+?){3}',text)
    matches = re.findall('(?:[а-яА-ЯѢѣі-]+[.,?:;]? ){3}[а-яА-ЯѢѣі-]*аго [а-яѢѣі-]+(?:а|я|и)[.,?:;]?(?: [а-яА-ЯѢѣі-]*[.,?;:]?){3}', text)
    print('\n'.join(matches))
    print('\n')
    print('\n'.join(agos))
    
final()
    
