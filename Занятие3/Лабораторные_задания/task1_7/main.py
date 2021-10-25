def ass_situation2(a, b, c):
    debit = a
    credit = b
    money = c + a - b
    i = 0
    print("1 месяц осталось денег =", money)
    while money + debit - credit * 1.05 >= 0:
        i += 1
        credit = credit * 1.05
        money = money + debit - credit
        print(i, " осталось денег =", money)


if __name__ == "__main__":
    ass_situation2(5000, 6000, 12000)