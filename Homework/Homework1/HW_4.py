# Task 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input('Enter int: '))
max_num = 0
while number > 1:
    comp_num = number % 10
    if comp_num > max_num:
        max_num = comp_num
    number = number//10
print(max_num)
