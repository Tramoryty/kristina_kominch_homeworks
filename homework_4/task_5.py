# 5) Пользователь вводит три числа. Если все числа больше 10, то вывести на экран yes,
# иначе no.

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
if number_1 > 10 and number_2 > 10 and number_3 > 10:
    print('Yes')
else:
    print('No')
