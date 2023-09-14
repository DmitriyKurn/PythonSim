# Показывает информацию в файле
def show_data(filename):
    print(«\nПП | ФИО | Телефон»)
with open(filename, «r», encoding=»utf-8″) as data:
print(data.read())
print(«»)

