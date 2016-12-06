f = open('freq.txt', 'r', encoding='utf-8')

# Задание 1
print('Все строки с союзами: ')
for line in f:
    line = line.strip()
    line = line.split(' | ')
    if line[1] == 'союз':
        print(' | '.join(line))

f.close()
