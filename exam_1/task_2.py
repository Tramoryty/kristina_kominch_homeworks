# 2.	Написать программу для вычисления значения выражений.
# Проверить правильность выполнения задания с помощью тестовых значений.

import math

alpha = int(input('Введите значение alpha: '))
beta = int(input('Введите значение beta: '))
gamma = int(input('Введите значение gamma: '))
y = 1 / 4 * (math.sin(alpha + beta - gamma) + math.sin(beta + gamma - alpha)
             + math.sin(gamma + alpha - beta) - math.sin(alpha + beta + gamma))
print(f'При введенных значениях:\nalpha = {alpha}\nbeta = {beta}\ngamma = {gamma}\ny = {y}')
