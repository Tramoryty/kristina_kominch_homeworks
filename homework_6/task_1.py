# 1) Казино. Компьютер генерирует числа от 1 до 10 и от 1 до двух соответственно.
# Цифры от 1 до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный, 2-черный).
# Пользователю дается 5 попыток угадать номер и цвет(Пример. Вводим с клавиатуры: 3 красный)
# В случае неудачи, вывести на экран правильную комбинацию.

import random

attempts = 5
while attempts > 0:
    number = random.randint(1, 10)
    color = random.randint(1, 2)

    print(f'Попытка №{abs(attempts-6)}')

    number_input = int(input("Введите число от 1 до 10: "))
    color_input = input("Введите цвет (красный или черный): ")
    if color_input == 'красный':
        color_input = 1
    else:
        color_input = 2

    if number_input == number and color_input == color:
        print('Ура! Вы отгадали!')
        break
    else:
        if color == 1:
            color_text = 'красный'
        else:
            color_text = 'черный'
        print(f'К сожалению, Вы не угадали.\nПравильный ответ: {number} {color_text}\n')
    attempts -= 1
if attempts == 0:
    print('Попытки закончились.')
