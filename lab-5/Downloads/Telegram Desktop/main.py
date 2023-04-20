
import random
def z1():
    a = []
    for i in range(5):
        a.append(random.randint(-100, 100))
    b = str(input("Введите число"))
    if b in list('a'):
        print (a,b,'Поздравляю, Вы угадали число')
    else:
        print(a,b,'нет такого числа')
import random

def z2():
    spisok = list('123456')
    for c in range(len(spisok)):
        if spisok[c-1] == spisok[c]:
            print("Значения совпадают")
    else:
        print("Значения не совпадают")

def z3():
    dni = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    kol = int(input('сколько дней выходных - '))
    for i in dni:
        print("Будни", *dni[:-kol])
        print("Выходные", *dni[-kol:])
        break

def z4():
    spisok_1 = ("Иванов", "Курпатов", "Сизин", "Лортв", "Жаммин", "Эшиль", "Копит", "Тригг", "Моксан", "Привел")
    spisok_2 = ("Кушнерова", "Кучерук", "Антонова", "Иванов", "Орит", "Каромит", "Шолтим", "Капрон", "Норман", "Хангук")
    kom = random.randint(1, 10)
    kom_1 = spisok_1[kom : kom -5]
    kom_2 = spisok_2[kom : kom +5]
    kmand = tuple(kom_2 + kom_1)
    print(kom_1)
    print(kom_2)
    print(kmand)
    print(len(kmand))
    print(sorted(kmand))
    if "Иванов" in kmand:
        print("Иванов есть в команде")
        print(kmand.count("Иванов"))
    else:
        print("Иванова нет в команде")

print("1 задание")
z1()
print("2 задание")
z2()
print("3 задание")
z3()
print("4 задание")
z4()
