def enum_a_or_b():
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_even = []
    list_no_even = []
    for i in list_:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_no_even.append(i)
    if len(list_even) > len(list_no_even):
        print(list_even, "четных больше")
    elif len(list_even) < len(list_no_even):
        print(list_no_even, "четных меньше")
    else:
        print("одинаково")



if __name__ == "__main__":
    enum_a_or_b()