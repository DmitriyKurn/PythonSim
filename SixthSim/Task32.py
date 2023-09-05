n=(int(input("Введите число N элементов: ")))
list_1=[]
for i in range(n):
    num = int(input("Введите num "))
    list_1.append(num)
print(list_1)

max = (int(input("Введите max: ")))
min = (int(input("Введите min: ")))

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')