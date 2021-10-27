def up_list(n, m):
    print(list(range(n, m)))
    sum_ = sum(range(n, m))
    len_ = len(range(n, m))
    average_ = int(round(sum_/len_))
    print(list(range(average_+1, average_ + len_+ 1)))


if __name__ == "__main__":
    up_list(13, 55)


# взять из старого через лист комприхеншен // переделать