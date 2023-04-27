countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин",
                      "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                      "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава",
                      "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                      "Северная Македония": "Скопье", "Сербия": "Белград"}
alpha_costs = {
    "авеинорст": 1,
    "дклмпу": 2,
    "бгёья": 3,
    "йы": 4,
    "жзхцч": 5,
    "шэю": 8,
    "фщъ": 10
}

word = input("Введите слово")
sum = 0
for alpha in word:
    for j in alpha_costs:
        if alpha in j:
            sum += alpha_costs[j]
print(sum)


print("z_1")
print(countries_dict)
print(countries_dict["Франция"])
for key, value in countries_dict.items():
    print(f"{key} - {value}")
print("z_2")


students_lang = {"Петров": ["английский", "китайский"],
                 "Иванов": ["французский", "китайский"],
                 "Крыс": ["французский"],
                 "Ромист": ["китайский"],
                 "Зоргав": ["английский"],
                 "Жолпук": ["французский", "китайский"]}
unique_langs = set()
chinese_stud = []
for name, langs in students_lang.items():
    for lang in langs:
        unique_langs.add(lang)
    if "китайский" in langs:
        chinese_stud.append(name)
uniq = list(unique_langs)
print(sorted(uniq))
print(chinese_stud)
