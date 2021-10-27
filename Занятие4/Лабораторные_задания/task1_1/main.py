def quad_esc(n, m):
    list_ = []
    n = int(n)
    m = int(m)
    for number in range(n, m):
        if n < number < m:
            number = number * number
            list_.append(number)
        print(list_)


if __name__ == "__main__":
    quad_esc(2.1, 6.2)

