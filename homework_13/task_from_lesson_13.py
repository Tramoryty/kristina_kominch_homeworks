# 3) Напишите программу, которая принимает на вход список
# чисел в одной строке и выводит на экран
# в одну строку значения, которые встречаются в нём более одного раза.


def digit_favorite(numbers):
    list_new = [i for i in numbers.split(' ') if numbers.split(' ').count(i) > 1]
    set_list = ' '.join(list(set(list_new)))
    print(f'Значения, которые встречаются в строке более одного раза: {set_list}')


digit_input = input('Введите разные числа через пробел: ')
digit_favorite(digit_input)
