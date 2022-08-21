    # задание 1

example_list = ["string", 5, 15.32, False, "True",[]]

for item  in example_list:
    print(type(item))

    # задание 2

    old_list = list(input("Укажите значения >>> "))
    new_list = []

    n = 0

    if len(old_list) % 2 == 0:
        while n < len(old_list):
            new_list.extend([old_list[n + 1], old_list[n]])
            n = n + 2
    else:
        while n < (len(old_list) - 1):
            new_list.extend([old_list[n + 1], old_list[n]])
            n = n + 2
        else:
            new_list.extend(old_list[len(old_list) - 1])

    print(new_list)

    # задание 3

    month = int(imput("Укажите какой месяц"))

    vesna = {3, 4, 5},
    leto = {6, 7, 8},
    osen = {9, 10, 11},
    zima = {12, 1, 2})

    for season, months in year_dict.items():
        if
    month in months:
    print(f"Время года = {season}")
break

# задание 4

stroka = input("Введите строку из нескольких слов").split()

for i, el in enumerate(stroka, 1):
    print(i, el[0:10])
