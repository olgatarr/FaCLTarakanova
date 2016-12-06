# Задание 2

f = open('freq.txt', 'r', encoding='utf-8')
lines = f.readlines()

print('Существительные женского рода единственного числа')
nouns = []
ipm = 0
for line in lines:
    line = line.strip()
    line = line.split(' | ')
    if 'сущ' in line[1]:
        nouns.append(line[0])
        ipm += float(line[2])
print(', '.join(nouns))
print('IPM - ', ipm)
f.close()
