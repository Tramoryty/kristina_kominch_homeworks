# 3) Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число - кол-во нечётных цифр.
# Строка - количество букв.
# Сделать проверку со всеми этими

import random


def my_function(element):
    if isinstance(element, tuple):
        for i in element:
            if isinstance(i, str):
                print(f'Слово из кортежа "{i}", его длина - {len(i)}.')
    elif isinstance(element, list):
        letter_count = 0
        number_count = 0
        for i in element:
            if isinstance(i, str):
                letter_count += sum(a.isalpha() for a in i)
            elif isinstance(i, int):
                number_count += 1
        print(f'Количество букв в списке: {letter_count}.\nКоличество чисел в списке: {number_count}')
    elif isinstance(element, int):
        odd_digits_count = 0
        for i in str(element):
            if int(i) % 2 != 0:
                odd_digits_count += 1
        print(f'Количество нечетных цифр числа: {odd_digits_count}')
    elif isinstance(element, str):
        letter_count_str = 0
        for i in element.lower():
            letter_count_str += sum(i.isalpha() for a in i)
        print(f'Количсетво букв в строке: {letter_count_str}')


test_tuple = ('cat', 'dog', 'horse', 7, 5, 69, 'bird', 65, 'rainbow')
print(f'Исходный кортеж: {test_tuple}')
my_function(test_tuple)

my_function(list(test_tuple))

my_function(int(input('Введите целое число: ')))

my_function(input('Введите текст: '))
