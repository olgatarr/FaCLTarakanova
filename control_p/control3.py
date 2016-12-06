f = open('freq.txt', 'r', encoding='utf-8')
lines = f.readlines()

# Задание 3
while True:
    found = False
    word = input('Введите слово: ')
    if word == '':
        print('Работа программы завершена.')
        break
    else:
        for line in lines:
            line = line.strip()
            line = line.split(' | ')
            if line[0] == word:
                print('Морфологическая информация: ', line[1])
                print('IPM: ', line[2])
                found = True
                break
        if found == False:
            print('В словаре нет такого слова. Попробуйте ввести другое.')

f.close()
