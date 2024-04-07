# 4) Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс
# этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.

import random

numbers = [random.randint(-100, 100) for i in range(20)]
print(f'Данный рандомный список из 20 элементов: {numbers}')

max_number = max(numbers)
index_max_number = numbers.index(max_number)

print(f'Наибольшее значение в данном списке: {max_number}')
print(f'Индекс наибольшего значения в данном списке: {index_max_number}')
