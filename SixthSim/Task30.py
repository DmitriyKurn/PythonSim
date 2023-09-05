a1 = int(input('Введите первый элемент: '))
n = int(input('Введите количество элементов: '))
d = int(input('Введите разность: '))

for i in range(n):
     print(a1 + i * d, end=' ')