# 2) Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами.
# Выведите полученный словарь на экран.

d = {'1': 0, '2': 0, '3': 0}

key_d = ['1', '2', '3']
value_d = [0, 0, 0]
d_1 = dict(zip(key_d, value_d))
print(f'Способ 1: {d_1}')

key_d_2_int = [i for i in range(1, 4)]
key_d_2 = []
for i in key_d_2_int:
    if type(i) == int:
        key_d_2.append(str(i))
value_d_2 = [0] * 3
d_2 = dict(zip(key_d_2, value_d_2))
print(f'Способ 2: {d_2}')

key_d_3 = ['1', '2', '3']
d_3 = dict.fromkeys(key_d_3, 0)
print(f'Способ 3: {d_3}')
