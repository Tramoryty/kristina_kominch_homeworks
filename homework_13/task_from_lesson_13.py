# 3) Напишите программу, которая принимает на вход список
# чисел в одной строке и выводит на экран
# в одну строку значения, которые встречаются в нём более одного раза.
import random


def digit_favorite(numbers):
    list_digit_favorite = numbers.split(' ')
    list_new = []
    for number in list_digit_favorite:
        if list_digit_favorite.count(number) > 1:
            list_new.append(number)
    set_list = ' '.join(list(set(list_new)))
    print(f'Значения, которые встречаются в строке более одного раза: {set_list}')


digit_input = input('Введите разные числа через пробел: ')
digit_favorite(digit_input)
