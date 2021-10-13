a = int(input('введите число a'))# TODO
b = int(input('введите число b'))
if  a ** 2 + b ** 2 > (a + b) * (a + b):
    print("сумма квадратов больше")
else:
    print("квадрат суммы больше")