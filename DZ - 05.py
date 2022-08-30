#ЗАДАНИЕ1

strings = []

while True:
with open ('task01.txt', 'a+') as f:
    string = input ("Введите строку")

    if not string:
        break

        f.write(f"{string\n}")


#ЗАДАНИЕ 2
with open('task02.txt') as f:
    rows = f.readlines()
    expanded_rows = [row.split() for row is rowns]

    rows_count, words_count = len(rows), sum([len(word_list) for word_list in expanded_rows])

    print(f"Всего строк - {rows_count}, всего слов - {words_count}")

# ЗАДАНИЕ 3
with open('task03.txt') as f:
worker_list = [woker_line.split() for worker_line in f.readlines()]

workers_with_info = [
    {"name": worker[0], "salary": float(worker[1])}
for worker in worker_list
if len (worker) > 1
]

#ЗАДАНИЕ 4

translation = {
    "one" : "Один"
    "two" : "Два"
    "There" : "Три"
    }

    converted_rous = []
    with open("task04.txt") as input_data:
        for row in input_data:
            name, value = row.split('_')
            converted_rous.append(f"{translations[name]} - {value}")
            with open("task04_ru.txt", "w") as output_data:
                output_data.writelines(converted_rous)









