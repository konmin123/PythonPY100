def search_number(number_list):
    numbers_list = numbers_list.split()
    for i in numbers_list:
        if i in range(3, 14) and i >= 0:
            print(i)
        elif i < 0:
            break


if __name__ == "__main__":
    search_number()