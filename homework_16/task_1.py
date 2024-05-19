# 1) Реализовать калькулятор с 4 методами:
# Сумма, вычитание , умножение, деление.
# Метод принимает 2 аргумента и возвращает результат.
# Невалидные данные должны быть обработаны(в классе написать проверку на валидность данных)

class Calculator:

    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return f'{self.num1} + {self.num2} = {self.num1 + self.num2}'

    def subtract(self):
        return f'{self.num1} - {self.num2} = {self.num1 - self.num2}'

    def multiply(self):
        return f'{self.num1} * {self.num2} = {self.num1 * self.num2}'

    def divide(self):
        try:
            return f'{self.num1} / {self.num2} = {self.num1 / self.num2}'
        except ZeroDivisionError:
            return 'Division by zero'

    def ceil_divide(self):
        try:
            return f'{self.num1} // {self.num2} = {self.num1 // self.num2}'
        except ZeroDivisionError:
            return 'Division by zero'

    def power(self):
        return f'{self.num1} ^ {self.num2} = {self.num1 ** self.num2}'

    def mod(self):
        return f'{self.num1} % {self.num2} = {self.num1 % self.num2}'


while True:
    number_1 = int(input('Enter first number: '))
    operation = input('Enter operation (+, -, *, /, //, **, %): ')
    number_2 = int(input('Enter second number: '))
    calculator = Calculator(number_1, number_2)

    if operation == 'stop':
        break
    elif operation == '+':
        print(calculator.sum())
    elif operation == '-':
        print(calculator.subtract())
    elif operation == '*':
        print(calculator.multiply())
    elif operation == '/':
        print(calculator.divide())
    elif operation == '//':
        print(calculator.ceil_divide())
    elif operation == '**':
        print(calculator.power())
    elif operation == '%':
        print(calculator.mod())


# class Calculator:
#
#     def __init__(self, num1: float, num2: float, operator):
#         self.num1 = num1
#         self.num2 = num2
#         self.operator = operator
#
#     def calculate(self):
#         if self.operator == '+':
#             return self.num1 + self.num2
#         elif self.operator == '-':
#             return self.num1 - self.num2
#         elif self.operator == '*':
#             return self.num1 * self.num2
#         elif self.operator == '/':
#             try:
#                 return self.num1 / self.num2
#             except ZeroDivisionError:
#                 return 'Division by zero'
#
#
# number_1 = float(input('Enter first number: '))
# op = input('Enter operation (+, -, *, /): ')
# number_2 = float(input('Enter second number: '))
# calculator = Calculator(number_1, number_2, op)
# print(f'Результат: {calculator.calculate()}')
