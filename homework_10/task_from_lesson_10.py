# 10. Дан список чисел [1, 2, 3, 20, 30, 45, 20, 100, 20], необходимо удалить все вхождения числа 20 из него.
list_1 = [1, 2, 3, 20, 30, 45, 20, 100, 20]
for i in list_1:
    if i == 20:
        list_1.remove(20)
print(list_1)


# 11. Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице
list_2 = [0] * 100
# list_2[0] = 1
# list_2[-1] = 1
for i in range(len(list_2)):
    if i == 0 or i == 99:
        list_2[i] = 1
print(list_2)


# 12. Сформировать возрастающий список из чётных чисел (количество элементов 45)
import random
list_3 = [random.randint(0, 100) * 2 for i in range(45)]
list_3.sort()
print(list_3)


# 13. Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]. Выведите все элементы, которые меньше 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)


# 14. Заполнить список степенями числа 2 (от 2^1 до 2^n)
n = int(input('Введите степень до которой нужно возводить число 2: '))
list_n = [2**i for i in range(1, n+1)]
print(list_n)

# 15. Дан словарь с числовыми ключами и значениями.
# Необходимо их все ключи перемножить а значения сложить и вывести на экран.

dict_1 = {i: random.randint(1, 100) for i in range(1, 11)}
keys_product = 1
for key in dict_1.keys():
    keys_product *= key
values_sum = sum(dict_1.values())
print(f'Исходный словарь: {dict_1}')
print(f'Произведение ключей: {keys_product}')
print(f'Сумма значений: {values_sum}')


# 16. Создайте словарь, в котором ключами будут числа от 1 до 10,
# а значениями эти же числа, возведенные в куб.
dict_2 = {i: i**3 for i in range(1, 11)}
print(dict_2)


# 17. Напишите программу, которая получает на
# вход две строки с перечислением интересов и хобби двух пользователей,
# и вычисляет процент совпадения.

hobby_input_1 = input('Пользователь 1, введите Ваши интересы и хобби, через запятую и пробел: ')
hobby_input_1.lower()
hobby_input_2 = input('Пользователь 2, введите Ваши интересы и хобби, через запятую и пробел: ')
hobby_input_2.lower()

list_hobby_1 = hobby_input_1.split(', ')
list_hobby_2 = hobby_input_2.split(', ')

common_hobbies = []

if len(list_hobby_1) >= len(list_hobby_2):
    for i in list_hobby_1:
        if i in list_hobby_2:
            common_hobbies.append(i)
            print(f'Процент совпадения интересов и хобби: {len(common_hobbies) / len(list_hobby_1) * 100}%')
elif len(list_hobby_1) < len(list_hobby_2):
    for i in list_hobby_2:
        if i in list_hobby_1:
            common_hobbies.append(i)
            print(f'Процент совпадения интересов и хобби: {len(common_hobbies) / len(list_hobby_2) * 100}%')
else:
    print('Совпадений интересов и хобии нет.')


# 18. Напишите программу, которая получает n слов, и вычисляет количество уникальных символов во всех словах.
input_string = input('Введите слова, разделённые запятой и пробелом: ')

words = input_string.split(', ')
words_string = ''.join(words)

letter_count = {}
for letter in words_string:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
unique_count = 0
for letter, count in letter_count.items():
    if count == 1:
        unique_count += 1
print(f'Количество уникальных силмволов в введенных словах {unique_count}')
