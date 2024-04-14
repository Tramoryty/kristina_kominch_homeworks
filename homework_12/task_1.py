# 1)Создайте функцию для определения наибольшего числа
import random


def digit_max(digits):
    max_digit = max(digits)
    print(f'Наибольшее число: {max_digit}')


list_digit = [random.randint(-100, 100) for i in range(20)]
print(f'Рандомный список чисел: {list_digit}')
digit_max(list_digit)
