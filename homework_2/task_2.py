# 2) Вычислить сумму цифр случайного трёхзначного числа (тут необходимо
# применить работу со строками)

import random

random_number = random.randint(100, 999)
print(f'Рандомное трёхзначное число: {random_number}')

random_number_str = str(random_number)
digit_1 = int(random_number_str[0]) #Первая цифра числа
digit_2 = int(random_number_str[1]) #Вторая цифра числа
digit_3 = int(random_number_str[2]) #Третья цифра числа

print(f'Сумма цифр этого числа: {digit_1+digit_2+digit_3}')
