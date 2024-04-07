# 3) Дан список чисел. Определите, сколько в этом списке элементов, которые больше
# двух своих соседей, и выведите количество таких элементов. Крайние элементы
# списка никогда не учитываются, поскольку у них недостаточно соседей.

import random

numbers = [random.randint(-100, 100) for i in range(20)]
print(f'Данный рандомный список из 20 элементов: {numbers}')
count = 0
for i in range(1, len(numbers) - 1):
    if numbers[i - 1] < numbers[i] > numbers[i + 1]:
        count += 1
print(f'В данном списке {count} элементов, которые больше двух своих соседей')
