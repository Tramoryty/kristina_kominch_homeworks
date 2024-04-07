# 1) Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и
# dictionary_2 = {'c': 500, 'd': 600}.
# Объедините их в один при помощи встроенных функций языка Python.

dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
print(dict(**dictionary_1, **dictionary_2))
print(dictionary_1 | dictionary_2)
