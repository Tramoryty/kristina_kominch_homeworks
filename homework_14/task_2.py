# 2) Создать текстовый файл, записать в него построчно
# данные, которые вводит пользователь. Окончанием ввода
# пусть служит пустая строка.
list_input = []
while True:
    i = input('Введите текст: ')
    if i == '':
        break
    else:
        list_input.append(i)

with open('task_2.txt', 'w', encoding='cp1251') as file:
    file.writelines((i + '\n') for i in list_input)
