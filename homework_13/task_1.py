# 1) Функция для вывода таблицы умножения для указанного числа

# это вторая задача из предыдущей домашки

def multiplication_table(num):
    for i in range(1, num + 1):
        print(f'{num} * {i} = {num * i}')


multiplication_table(int(input('Введите число: ')))
