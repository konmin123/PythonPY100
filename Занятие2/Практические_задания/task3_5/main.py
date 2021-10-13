wind = int(input())

if wind in range(1,5):# TODO напишите с помощью if-elif-else условие проверки скорости ветра
    print('слабый')
elif wind in range(5, 10):
    print('умеренный')
elif wind in range(11,18):
    print('сильный')
elif wind >= 19:
    print('ураганный')
else:
    print('введите корр')