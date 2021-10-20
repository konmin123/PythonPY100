def blabla():
    max_sum = 500
    current_sum = 0
    n = 1
    pow_ = 2
    while current_sum <= max_sum:
        current_sum += n ** pow_
        print("число", n, "сумма чисел", current_sum)
        n = n + 1
    return n


if __name__ == "__main__":
    blabla()


