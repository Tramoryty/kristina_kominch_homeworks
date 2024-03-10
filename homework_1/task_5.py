# 5) Вычислить сумму цифр случайного трёхзначного числа.(прочитать про
# модуль math и random)

import random

random_number = random.randint(100, 999)

digit_1 = random_number//100 #Первая цифра числа
digit_2 = (random_number//10) % 10 #Вторая цифра числа
digit_3 = random_number % 10 #Третья цифра числа

print('Случайное трехзначное число:', random_number)
print('Сумма цифр этого числа:', digit_1+digit_2+digit_3)
