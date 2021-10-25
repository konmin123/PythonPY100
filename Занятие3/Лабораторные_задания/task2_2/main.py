def str_poli(str1):
    str2 = str1[::-1]
    if str1 == str2:
        print("введена строка палиндром")
    else:
        print("эта строка палиндромом не является")


if __name__ == "__main__":
    str_poli("12321")
