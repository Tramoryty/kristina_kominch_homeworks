# 12.	С клавиатуры вводится десятизначное число.
# Вывести на экран четные числа входящие в данное число.
# Например 1234567892  2 4 6 7 8 2

ten_digit_number = input('Введите десятизначное число: ')
for digit in ten_digit_number:
    if len(ten_digit_number) == 10:
        if int(digit) % 2 == 0:
            print(digit)
    else:
        print('Вы ввели не десятизначное число')
        break
