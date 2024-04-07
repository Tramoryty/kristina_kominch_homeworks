import random

# 1) Даны два кортежа. Требуется объединить их между собой.
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
print(tuple_1 + tuple_2)


# 2) В кортеже целых чисел найдите максимальный и минимальный элементы, а также осуществите их обмен.
numbers_tuple = tuple(random.randint(1, 100) for _ in range(10))
print(f'Исходный кортеж: {numbers_tuple}')

numbers = list(numbers_tuple)
min_index = 0
max_index = 0
for i in range(len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i
    elif numbers[i] > numbers[max_index]:
        max_index = i
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

new_numbers_tuple = tuple(numbers)
print(f'Кортеж, в котором min и max элементы поменяны местами: {new_numbers_tuple}')


# 3) В список, сгенерированный случайным образом, добавить введенный
# пользователем элемент.
numbers = [random.randint(1, 100) for _ in range(10)]
print(f'Исходный список:{numbers}')
el_input = int(input('Введите любое целое число: '))
numbers.append(el_input)
print(f'Новый список:{numbers}')


# 4) В список, сгенерированный случайным образом, добавить введенный
# пользователем элемент на указанную позицию.
numbers2 = [random.randint(1, 100) for _ in range(10)]
print(f'Исходный список:{numbers2}')
el_input2 = int(input('Введите любое целое число: '))
in_input = int(input('Укажите номер индекса от 0 до 11, на который нужно поместить новый элемент: '))
numbers2.insert(in_input, el_input2)
print(f'Новый список:{numbers2}')


# 5) Имеются два списка, сгенерированные случайным образом. Добавьте в
# конец первого списка все элементы второго списка.
print(numbers + numbers2)


# 6) Из заранее сформированного списка следует удалить элемент, введенный
# пользователем.
list1 = [i for i in range(1, 11)]
print(f'Исходный список: {list1}')
int_input = int(input('Введите число от 1 до 10, которое нужно удалить из списка: '))
list1.remove(int_input)
print(f'Список с удаленным элементом: {list1}')


# 7) Из исходного списка следует удалить элемент, позицию которого указал
# пользователь.
list2 = [i for i in range(1, 11)]
print(f'Исходный список: {list2}')
int_input2 = int(input('Введите индекс числа, которое нужно удалить из списка: '))
list2.pop(int_input2)
print(f'Список с удаленным элементом: {list2}')


# 8) В кортеже целых чисел вычислите произведение отрицательных
# элементов, имеющих нечетные индексы
numbers_tuple_2 = tuple(random.randint(-100, 100) for _ in range(20))
print(f'Исходный кортеж: {numbers_tuple_2}')

numbers_2 = list(numbers_tuple_2)
new_numbers_2 = 1
for i in range(len(numbers_2)):
    if numbers_2[i] < 0 and i % 2 != 0:
        new_numbers_2 *= numbers_2[i]
print(f'Произведение отрицательных элементов кортежа на нечетных индексах: {new_numbers_2}')


# 9) Заполните один кортеж десятью случайными целыми числами от 0 до 5
# включительно. Также заполните второй кортеж числами от -5 до 0.
# Объедините два кортежа с помощью оператора +, создав тем самым третий
# кортеж. С помощью метода кортежа count() определите в нем количество
# нулей. Выведите на экран третий кортеж и количество нулей в нем.
tuple3 = tuple(i for i in range(0, 6))
tuple4 = tuple(i for i in range(-5, 1))
tuple5 = tuple3 + tuple4
print(f'Объединенный кортеж: {tuple5}')
print(f'Количество 0 в данном кортеде: {tuple5.count(0)}')


# 10) Вывести данные кортежа без скобок, через запятую. Обязательно:
# элементы кортежа – строки.
tuple6 = ('afd', 'bhdhd', 'cfju', 'dkiu')
list6 = list(tuple6)
print(', '.join(list6))


# 11) Сгенерируйте 2 кортежа случайными числами в диапазоне от 10-90.
# Количество элементов в кортеже 10. Определить: 1) Сумма элементов какого
# из кортежей больше и вывести соответствующее сообщение на экран (
# Сумма больше в кортеже - ..) 2) Вывести на экран порядковые номера
# минимальных элементов этих кортежей
numbers_tuple_3 = tuple(random.randint(10, 90) for _ in range(10))
print(numbers_tuple_3)
numbers_tuple_4 = tuple(random.randint(10, 90) for _ in range(10))
print(numbers_tuple_4)
if sum(numbers_tuple_3) > sum(numbers_tuple_4):
    print(f'Сумма элементов больше в кортеже: {numbers_tuple_3}.')
elif sum(numbers_tuple_3) < sum(numbers_tuple_4):
    print(f'Сумма элементов больше в кортеже: {numbers_tuple_4}.')
min_tuple_3 = min(numbers_tuple_3)
print(min_tuple_3)
min_tuple_4 = min(numbers_tuple_4)
print(min_tuple_4)
