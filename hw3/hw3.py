print('Введите три числа:')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a*b == c:
    print(a, '*', b, ' = ', c)
else:
    print(a, '*', b, ' != ', c)
    print(a, '*', b, ' = ', a*b, '\n')
if a/b == c:
    print(a, '/', b, ' = ', c)
else:
    print(a, '/', b, ' != ', c)
    print(a, '/', b, ' = ', a/b)

