# 1) Определить, является ли год високосным.

year = int(input('Введите год, чтобы проверить является ли он високосным: '))

if year % 4 == 0:
    print(f'{year} - является високосным.')
else:
    print(f'{year} - не является високосным.')
