# 11.	Дан список чисел, необходимо удалить все вхождения числа 20 из него.

import random

list_numbers = [random.randint(15, 25) for i in range(20)]
print(f'Исходный список: {list_numbers}')

while 20 in list_numbers:
    list_numbers.remove(20)
print(f'Список с удаленными ччислами 20: {list_numbers}')
