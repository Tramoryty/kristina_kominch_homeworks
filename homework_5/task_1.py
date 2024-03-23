# 1)Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное,
# то посчитать сумму его цифр. - результат число
# Если нечётное, то заменить его на 1 в списке. - результат список
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

list1 = [15, 48, 'hello', 6, 19, 'world']
print(f'Данный список: {list1}')

for i in list1:
    if isinstance(i, int) and i % 2 == 0:
        sum_digits = sum(int(i) for i in str(i))
        print(f'Сумма цифр четного числа из списка "{i}": {sum_digits}')

list2 = []
for i in list1:
    if isinstance(i, int) and i % 2 != 0:
        list2.append(1)
    else:
        list2.append(i)
print(f'Список, в котором нечетные числа заменены на 1: {list2}')

for i in list1:
    if isinstance(i, str):
        vowels = 'eyuioa'
        vowel_count = 0
        for a in i:
            if a in vowels:
                vowel_count += 1
        print(f'Количество гласных в слове "{i}" = {vowel_count}, негласных = {len(i)-vowel_count}')
