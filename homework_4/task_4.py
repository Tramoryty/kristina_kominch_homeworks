# 4) Напишите программу, которая выполняет сравнение двух переменных.

number_1 = int(input('Введите первое число для сравнения: '))
number_2 = int(input('Введите второе число для сравнения: '))
if number_1 > number_2:
    print(f'Число {number_1} больше числа {number_2}.')
elif number_1 < number_2:
    print(f'Число {number_1} меньше числа {number_2}.')
else:
    print(f'Числа {number_1} и {number_2} равны.')
