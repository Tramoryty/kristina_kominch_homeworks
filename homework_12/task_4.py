# 4) Простейший калькулятор с введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: "Деление на ноль"
# Ноль использовать в качестве завершения программы (сделать как отдельную

def calculator():
    while True:
        try:
            num1 = float(input('Введите первое число: '))
            operator = input('Введите действие (+ - * /). Для завершения программы введите 0: ')
            num2 = float(input('Введите второе число: '))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            elif operator == '0':
                break
            else:
                continue
        except ZeroDivisionError:
            print('На 0 делить нельзя, попробуйте ещё раз.')
        else:
            print(f'Ваша задача и результат: {num1} {operator} {num2} = {result}')


calculator()
