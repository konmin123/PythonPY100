def search_sequence():
    sum_number = 0
    number = 1
    while number != 0:
        number = int(input('введите число'))
        if number > 0:
            sum_number = sum_number + number
            print(sum_number)
    print("итоговая сумма =", sum_number)


if __name__ == "__main__":
    search_sequence()
