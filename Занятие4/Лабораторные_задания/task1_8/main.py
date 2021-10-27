def new_list():
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print([i ** 3 if i < 0 else i for i in list_])


if __name__ == "__main__":
    new_list()