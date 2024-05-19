# 3) Задача на декоратор
#
# метод sum(a, b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку
# если переданы не числовые параметры(например строка)
# пример:
#
# @validate_int_parameters
# def sum(a,b)`
#
# sum(3, "1") => ошибка
# sum(4, 2) = > 6

def validate_parameters(func):
    def wrapper(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return ValueError('Оба параметра должны быть числами')
        return func(a, b)
    return wrapper


@validate_parameters
def sum_ab(a, b):
    return f'Сумма: {a + b}'


print(sum_ab(4, '2'))
print(sum_ab(4.5, 2.5))
