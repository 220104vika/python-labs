def F(numb: int):
    return True if numb % 3 == 0 else False


def G(chisl):
    res = None
    try:
        res = 100 / float(chisl)
    except ValueError:
        print("Нужно ввести число")
    except ZeroDivisionError:
        print("Нужно ввести число отличное от 0")
    return res

def M(date):
    date = date.split('.')
    Vag_date = int(date[0])*int(date[1]) == int(date[2][2:4])
    print(Vag_date)

def P(nomer:str):
    sum1 = ([int(i) for i in nomer[:int(len(nomer) / 2)]])
    sum2 = sum([int(i) for i in nomer[int(len(nomer) / 2):]])
    if sum1 == sum2:
        return True
    else:
        return False

print("Проверка деления на 3")
print(F(13))
print(F(21))

print("Деление 100 на число")
print(G(10))
print(G(78))

print("Магическая дата")
print(M("12.12.2023"))
print(M("22.01.2022"))
print(M("21.01.2022"))

print("Счастливый билет")
print(P("234567"))
print(P("111111"))