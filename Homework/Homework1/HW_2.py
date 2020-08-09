# Task 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.
time = int(input('Enter time in seconds: '))
hour = time//3600
minute = time//60 - hour*60
second = time%60
print(F"{hour:02}:{minute:02}:{second:02}")