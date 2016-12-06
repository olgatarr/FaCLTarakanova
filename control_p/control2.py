# Задание 2

f = open('freq.txt', 'r', encoding='utf-8')
lines = f.readlines()

nouns = []
ipm = 0
for line in lines:
    line = line.strip()
    line = line.split(' | ')
    if 'сущ' in line[1]:
        nouns.append(line[0])
        ipm += float(line[2])
print('Существительные женского рода единственного числа: ', ', '.join(nouns))
print('Сумма IPM - ', ipm)
f.close()
