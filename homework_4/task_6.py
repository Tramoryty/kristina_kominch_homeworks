# 6) Пользователь вводит два числа с клавиатуры. Вывести на экран yes, если они отличаются
# друг от друга на 135,
# иначе вывести на экран No;

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
if number_1 - number_2 == 135 or number_2 - number_1 == 135:
    print('Yes')
else:
    print('No')