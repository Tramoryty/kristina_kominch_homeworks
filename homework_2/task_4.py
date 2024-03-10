# 4) Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым и
# вывести на экран. Затем объединить элементы с использованием пробела,
# чтобы программа вывела “Apples Oranges Pears Bananas Berries”.

string = 'Apples, Oranges, Pears, Bananas, Berries'
print(f'Исходная строка: {string}')

print(f'Строка разделена по ", " в список: {string.split(', ')}')

print(f'Элементы списка объеденены в строку: {" ".join(string.split(', '))}')
