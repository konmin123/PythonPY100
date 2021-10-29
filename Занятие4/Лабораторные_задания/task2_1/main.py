def number_n(n):
    list_str = list(str(n))   # задача 1
    list_digits = list_str
    for i, x in enumerate(list_digits):  # задание 2
        list_digits[i] = int(x)
    sum_digits = sum(list_digits)
    sum_even = 0                        # Задание 3
    for digit in list_digits:
        if digit % 2 == 0:
            sum_even = sum_even + digit
    stake_numbers = 0                   # Задание 4
    for i in list_digits:
        stake_numbers += 1
    min_number = min(list_digits)       # Задание 5
    max_number = max(list_digits)       # Задание 5
    list_even_positions = []            # Задание 6
    for index, i in enumerate(list_digits):
        if index % 2 != 0:
            list_even_positions.append(i)
    diff = list_digits[0] - list_digits[-1]     # Задание 7
    min_position = []                           # Задание 8
    for index, i in enumerate(list_digits):
        if index == min(list_digits):
            min_position.append(i)

    print(list_str, sum_digits, sum_even, stake_numbers, min_number, max_number, list_even_positions, diff, min_position)



if __name__ == "__main__":
    number_n(106)

