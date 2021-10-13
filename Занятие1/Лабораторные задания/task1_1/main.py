DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input('Внесите свой год рождения'))  # TODO запросить у пользователя год рождения
current_year = int(input('Внесите текущий год'))  # TODO запросить у пользователя текущий год

old_user_on_day =(current_year - start_year)*365 # TODO посчитать и распечатать количество прожитых дней
print(old_user_on_day)