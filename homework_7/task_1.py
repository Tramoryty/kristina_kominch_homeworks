# 1) Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

import random

numbers = [random.randint(1, 100) for i in range(20)]
print(f'Исходный рандомный список из 20 чисел: {numbers}')
new_numbers = []
for i in range(len(numbers)):
    if numbers[i] > numbers[i-1]:
        new_numbers.append(numbers[i])
for i in new_numbers:
    print(f'Элемент, который больше предыдущего элемента: {i}')
