def extract(name):
    f = open(name, 'r', encoding='cp1251')
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = lines[i].lower().strip().split(';')
    return lines       

def make_dic(lines):
    dic = {}
    for line in lines:
        dic[line[0].strip()] = line[1].strip()
    return dic

def guess(dic):
    for ngram in dic:
        print(ngram, ' ', '.'*len(dic[ngram]))
        guess = input('Введите слово: ')
        if guess == dic[ngram]:
            print('Правильно!')
        else:
            print('Неправильно!')

    
def final():
    lines = extract('lines.csv')
    dic = make_dic(lines)
    guess(dic)

final()
