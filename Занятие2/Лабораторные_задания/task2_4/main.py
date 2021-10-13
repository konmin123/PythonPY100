if __name__ == "__main__":
    text_ = "Hello,world"  # постарайтесь не использовать "магические" числа,
     # а по возможности дать переменным осмысленные названия и использовать их
    for index, volue in enumerate(text_, start=4):  # TODO Распечатать строку лесенкой
        print(" " * index, volue)



        #for index, value in enumerate(rus_alphabet, start=1)