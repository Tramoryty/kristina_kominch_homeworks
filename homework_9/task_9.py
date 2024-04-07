# 9) Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные.
# Результат вывести в виде кортежа.

string_input = input('Введите строку: ')
string = ()
for i in range(len(string_input)):
    if string_input[i] not in string:
        string += (string_input[i],)
print(string)
