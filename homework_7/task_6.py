# 6) В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент
# этого списка.

import random

numbers = random.sample(range(1, 100), 10)
print(f'Данный рандомный список из 10 элементов: {numbers}')

min_index = 0
max_index = 0

for i in range(len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i
    elif numbers[i] > numbers[max_index]:
        max_index = i

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(f'Список, в котором min и max элементы поменяны местами: {numbers}')
