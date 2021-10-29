def diff():
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    sum_ = sum(list_)
    len_ = len(list_)
    average = sum_ / len_
    print([i - average for i in list_])


if __name__ == "__main__":
    diff()
