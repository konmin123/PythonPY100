def easy_mn(a):
    i = 2
    a = a
    while i <= a:
        if a % i == 0:
            a = a // i
            print(i)
        else:
            i += 1


if __name__ == "__main__":
    easy_mn(2)
