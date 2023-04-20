mest = int(input())
if mest <= 36 and mest % 2 == 0:
    print("Плацкартное место, верхняя полка")
elif mest <= 36 and mest % 2 != 0:
    print("Плацкартное место, нижняя полка")
elif mest > 36 and mest < 56:
    print("Плацкартное место, боковая полка")