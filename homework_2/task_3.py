# 3) На вход подается непустая строка S. В строке хотя бы два символа.
# 1) В первой строке распечатайте каждый 3-й символ, начиная с нулевого
# (подряд, не разделяя символы пробелами).
# 2) Во второй строке распечатайте первый и последний символы (подряд,
# не разделяя символы пробелами).
# 3) В третей строке распечатайте S в верхнем регистре.
# 4) В четвертой строке распечатайте S в обратном порядке.
# 5) В пятой строке напечатайте True, если все символы в строке S — цифры
# и False в противном случае.

S = input("Напишите пару слов о себе: ")

#1
print(f'Каждый третий символ введенных данных: {S[::3]}')

#2
print(f'Первый и последний символы введенных данных: {S[0]+S[-1]}')

#3
print(f'"О Вас" в верхнем регистре: {S.upper()}')

#4
print(f'"О Вас" в обратном порядке: {S[::-1]}')

#5
print(f'Вы использовали только цифры при написании?: {S.isdigit()}')
