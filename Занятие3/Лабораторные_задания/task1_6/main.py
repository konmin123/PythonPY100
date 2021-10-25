def ass_situation(a, b):
    debit = a
    credit = b
    sum_debit = b - a
    print("1 месяц задолженнось =", sum_debit)
    for i in range(2, 11):
        credit = credit * 1.03
        sum_debit = sum_debit + (credit - debit)
        print(i, " месяц задолженнось =", sum_debit)


if __name__ == "__main__":
    ass_situation(5000, 6000)