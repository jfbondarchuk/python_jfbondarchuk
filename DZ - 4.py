# ЗАДАНИЕ 1

import sys

_, work_hours, hour_cost, bonus = sys.argv
salary = (float(hour_cost)) * (float(work_hours)) + float(bonus)
print(f"Зарплата = {salary}")

# ЗАДАНИЕ 2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [
    val for idx, val in enumerate(nambers)
    if idx > 0 and numbers[idx-1] < val
]

print(result_list)

# ЗАДАНИЕ 3

print ([
    x for x in range (20, 240)
    if x %20 == 0 or x % 21 == 0
])

# ЗАДАНИЕ 4

numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
items = [x for x in numbers if numbers.count(x) == 1]

print(items)

# ЗАДАНИЕ 5

from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("Список четных чисел [100..1000]:\n", list)
print("Произведение всего списка :\n", reduce(lambda a, b: a * b, list))

# ЗАДАНИЕ 6

#первый иттератор

print("*" * 10,"Иттерратор 1")
start_itterator = 3

for el in count(start_itterator):
    if el > 5
        break

        print(el)

#второй иттератор

print("*" * 10,"Иттерратор 2")
cycing_list = [2, 5, 7, 12]
max_itteretion = 8
itteration_count = 0

for el in cycle(cycing_list):
    print(el)
       itteration_count += 1

# ЗАДАНИЕ 7

def fact(n: int):
temp_result = 1

if number <= 0
    yield temp_result

    for x in range(1, number + 1):
        temp_result *= x
        yield temp_result

        n = 2

        for el in fact(n):
            print(el)




