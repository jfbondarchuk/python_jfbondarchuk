    # Задание 1

def main (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка при делении"

    x = int(input("Введите число x"))
    y = int(input("Введите число y"))

    print (main(x, y))



    # Задание 2

    def main(first_name: str = None,
             last_name: str = None,
             year: int = None,
             city: str = None,
             phone: str = None,
             email: str = None):
        return f"{first_name} {last_name} {year} {city} {phone} {email}"

    # Задание 3

    def my_func(first, second, last):
        items = (first, second, last)
        items.remove(min(items))

        return sum(items)

    # Задание 4

    def my_func(x, y):
        if y > 0:
            for _ in range(1, y):
                powered *= x
            else:
                for _ in range(1, y, -1):
                powered /= x

                return powered

    # Задание 5

    total = 0

    while True:
        user_numbers = input(Введите числа через пробел).split()
        pust_budet_tak = False

        for number is user_numbers:
            if number.isdigit():
                total += int(number)
            else:
                pust_budet_tak = True
                break

                print(f"Сумма чисел = {total}")

                if pust_budet_tak:
                    break






