# 6) Создать произвольный словарь 2. Добавить новый элемент с ключом типа str и значением
# типа int 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# 4. Получить элемент по ключу 5. Удалить элемент по ключу
# 6. Получить список ключей словаря

import random

keys = [i for i in range(1, 6)]
values = [random.randint(10, 99) for _ in range(5)]
dictionary = dict(zip(keys, values))
print(dictionary)

key_input = input('Введите наименование нового ключа: ')
value_input = int(input('Введите целое числовое значение для нового ключа: '))
dictionary_input = {key_input: value_input}
dictionary.update(dictionary_input)
print(dictionary)

numbers_tuple = tuple(random.randint(10, 90) for _ in range(3))
numbers_list = list(random.randint(10, 90) for _ in range(3))
dictionary_tuple_list = {numbers_tuple: numbers_list}
dictionary.update(dictionary_tuple_list)
print(dictionary)

print(dictionary.get(numbers_tuple))

dictionary.pop(numbers_tuple)
print(dictionary)

print(dictionary.keys())
