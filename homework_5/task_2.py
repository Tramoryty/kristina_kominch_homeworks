# 2) Даны 2 списка: a = [4,6,'pу','tell',78] b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
#     1)Сложить два списка
#     2) Добавьте число 6 на 3 позицию.
#     3)Удалите все текстовые элементы списка
#     4) Посчитайте количество элементов списка

a = [4, 6, 'pу', 'tell', 78,]
b = [44, 'hello', 56, 'exept', 3]

# 1)
new_list = a + b
print(f'Сумма двух списков: {new_list}')

# 2)
new_list.insert(2, 6)
print(f'Суммированный список с 6 на третьем месте: {new_list}')

# 3)
new_list_int = []
for i in new_list:
    # почему-то не удаляет слово 'tell' именно на этом месте, если на другом,
    # то работает, не поняла почему, поэтому через новый сделала
    # if isinstance(i, str):
    #     new_list.remove(i)
    if isinstance(i, int):
        new_list_int.append(i)
print(f'Список без слов: {new_list_int}')

# 4)
print(f'Количество элементов в списке: {len(new_list_int)}')
