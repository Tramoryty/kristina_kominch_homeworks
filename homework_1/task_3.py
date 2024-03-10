# 3) Даны два действительных числа. Найти среднее арифметическое и
# среднее геометрическое этих чисел.

import math

a = int(input('Введите первое целое число для расчета: '))
b = int(input('Введите второе целое число для расчета: '))

numbers = [a, b]

average_arithmetic = int(sum(numbers)/len(numbers))
print('\nСреднее арифметическое Ваших чисел:', average_arithmetic)

# math.prod вычисляет произведение элементов списка
average_geometric = math.prod(numbers) ** (1/len(numbers)) # Корень - это возведение в степень "1/на нужную степень корня"
print('Среднее геометрическое Ваших чисел:', round(average_geometric, 2))
