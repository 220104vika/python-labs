pas = input("Введите пароль")
is_numeric = False
is_upper = False
is_lower = False
is_spet = False
for char in pas:
    if char.isnumeric():
        is_numeric = True
    elif char.isupper():
        is_upper = True
    elif char.islower():
        is_lower = True
    elif char in "@#$%":
        is_spet = True
if len(pas) > 5 and is_numeric and is_upper and is_lower and is_spet:
    print("Пароль подходит")
else:
    print("Пароль говно")
pas_povtor = input("Повторите пароль")
if pas == pas_povtor:
    print("Пароль Верный")
else:
    print("Пароль неверный")