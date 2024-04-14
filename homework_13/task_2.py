# 2)На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа, которые больше 5 по модулю.

import random


def more_than_five(lst):
    new_lst = [i for i in lst if abs(i) > 5]
    print(f'Новый список, в котором только те числа, которые больше 5 по модулю:\n{new_lst}')


list_random = [random.randint(-10, 10) for i in range(30)]
print(f'Исходный список:\n{list_random}')
more_than_five(list_random)
