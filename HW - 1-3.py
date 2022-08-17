user_input = input("Введите число")

if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

    result = 0
    for x in range(1, 4):
        result += int(user_input * x)

        print(result)

   user_number = int(user_input):
        characters_count = 0
        team_number = user_number

    while temp_number:
        team_number //= 10
        characters_count += 1

        first_level_multiplication = (10 ** characters_count) + 2
        second_level_multiplication = (10 ** (characters_count * 2)) + ferst_level_multiplication
        result = user_number + (user_number * first_level_multiplication) + (user_number * second_level_multiplication)

        print(result)
